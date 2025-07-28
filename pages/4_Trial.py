import streamlit as st
import pandas as pd
from io import BytesIO
import tempfile
from sdv.metadata import Metadata
from sdv.single_table import (
    CTGANSynthesizer,
    TVAESynthesizer,
    GaussianCopulaSynthesizer,
    CopulaGANSynthesizer
)
import warnings
from sklearn.exceptions import ConvergenceWarning

# Suppress convergence warnings
warnings.filterwarnings("ignore", category=ConvergenceWarning)

st.set_page_config(page_title="Synthetic Data Generator", layout="wide")
st.title("🧬 Synthetic Data Generator App")

# ===============================
# 1. Upload CSV
# ===============================
uploaded_file = st.file_uploader("📁 Upload your CSV dataset", type=["csv"])

if uploaded_file is not None:
    original = pd.read_csv(uploaded_file)
    st.success(f"✅ Dataset uploaded with shape {original.shape}")
    st.dataframe(original.head())

    # ===============================
    # 2. Option to Upload Metadata JSON
    # ===============================
    st.markdown("### ⚙️ Metadata Options")
    uploaded_metadata = st.file_uploader("Optional: Upload your existing metadata JSON", type=["json"])

    if uploaded_metadata is not None:
        metadata = Metadata.load_from_json(uploaded_metadata)
        st.success("✅ Existing metadata loaded from JSON.")
    else:
        metadata = None  # We'll generate it if not provided

    # ===============================
    # 3. User Inputs
    # ===============================
    num_rows = st.number_input("🔢 How many synthetic rows to generate?", min_value=10, value=len(original))
    target_variable = st.text_input("🎯 Optional: What is your target variable? (Leave blank if none)")

    if st.button("🚀 Generate Synthetic Data"):

        # ===============================
        # 4. Generate Metadata (if not uploaded)
        # ===============================
        if metadata is None:
            with st.spinner("🔍 Generating metadata from uploaded dataset..."):
                metadata = Metadata.detect_from_dataframe(
                    data=original,
                    table_name='user_dataset',
                    infer_sdtypes=True,
                    infer_keys='primary_only'
                )
            st.success("✅ Metadata successfully generated!")
            st.info("📊 Proceeding to model training...")

        # ===============================
        # 5. Allow Download of Metadata JSON
        # ===============================
        with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as tmp_file:
            temp_json_path = tmp_file.name
            metadata.save_to_json(filepath=temp_json_path, mode="overwrite")

        with open(temp_json_path, "rb") as f:
            metadata_bytes = f.read()

        st.download_button(
            label="📥 Download Metadata JSON",
            data=metadata_bytes,
            file_name="metadata.json",
            mime="application/json"
        )

        # ===============================
        # 6. Train Synthesizers (With Safe Error Handling)
        # ===============================
        with st.spinner("🧠 Training synthesizers and generating synthetic data..."):
            models = {
                "CTGAN": CTGANSynthesizer(metadata, epochs=10, verbose=False),
                "TVAE": TVAESynthesizer(metadata, enforce_min_max_values=True, enforce_rounding=True, epochs=10),
                "GaussianCopula": GaussianCopulaSynthesizer(metadata, enforce_min_max_values=True, enforce_rounding=True, default_distribution='beta'),
                "CopulaGAN": CopulaGANSynthesizer(metadata, enforce_min_max_values=True, enforce_rounding=True, epochs=10, verbose=False),
            }

            synthetic_data_dict = {}
            failed_models = []

            for name, model in models.items():
                with st.spinner(f"Training {name}..."):
                    try:
                        with warnings.catch_warnings():
                            warnings.filterwarnings("ignore", category=ConvergenceWarning)
                            model.fit(original)
                        synthetic = model.sample(num_rows)
                        synthetic_data_dict[name] = synthetic
                        st.success(f"✅ {name} synthetic data created!")
                    except Exception as e:
                        failed_models.append((name, str(e)))
                        st.warning(f"⚠️ {name} failed: {e}")

        # ===============================
        # 7. Save Synthetic Data to Excel
        # ===============================
        if synthetic_data_dict:
            output = BytesIO()
            with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                for name, df in synthetic_data_dict.items():
                    df.to_excel(writer, sheet_name=name, index=False)
            output.seek(0)

            # ===============================
            # 8. Download Excel File
            # ===============================
            st.success("🎉 Synthetic datasets generated!")
            st.download_button(
                label="📥 Download Excel File with All Synthetic Datasets",
                data=output,
                file_name="synthetic_datasets.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

        # ===============================
        # 9. Optional Target Variable Preview
        # ===============================
        if target_variable and target_variable in original.columns:
            st.subheader("🎯 Target Variable Preview")
            for name, df in synthetic_data_dict.items():
                st.markdown(f"**{name}**")
                st.dataframe(df[target_variable].value_counts())

        # ===============================
        # 10. Show Summary of Failures
        # ===============================
        if failed_models:
            st.markdown("### ❌ Models That Failed to Train")
            for name, error in failed_models:
                st.error(f"**{name}**: {error}")
