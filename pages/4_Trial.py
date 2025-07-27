import streamlit as st
import pandas as pd
from io import BytesIO
from sdv.metadata import Metadata
from sdv.single_table import (
    CTGANSynthesizer,
    TVAESynthesizer,
    GaussianCopulaSynthesizer,
    CopulaGANSynthesizer
)

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
        metadata_bytes = BytesIO()
        metadata.save_to_json(metadata_bytes)
        metadata_bytes.seek(0)

        st.download_button(
            label="📥 Download Metadata JSON",
            data=metadata_bytes,
            file_name="metadata.json",
            mime="application/json"
        )

        # ===============================
        # 6. Train Synthesizers
        # ===============================
        with st.spinner("🧠 Training synthesizers and generating synthetic data..."):
            models = {
                "CTGAN": CTGANSynthesizer(metadata, epochs=10, verbose=False),
                "TVAE": TVAESynthesizer(metadata, enforce_min_max_values=True, enforce_rounding=True, epochs=10),
                "GaussianCopula": GaussianCopulaSynthesizer(metadata, enforce_min_max_values=True, enforce_rounding=True, default_distribution='beta'),
                "CopulaGAN": CopulaGANSynthesizer(metadata, enforce_min_max_values=True, enforce_rounding=True, epochs=10, verbose=False),
            }

            synthetic_data_dict = {}
            for name, model in models.items():
                model.fit(original)
                synthetic = model.sample(num_rows)
                synthetic_data_dict[name] = synthetic

            # ===============================
            # 7. Save Synthetic Data to Excel
            # ===============================
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

