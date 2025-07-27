import streamlit as st
import pandas as pd
from io import BytesIO
from sdv.metadata import SingleTableMetadata
from sdv.single_table import CTGANSynthesizer, TVAESynthesizer, GaussianCopulaSynthesizer, CopulaGANSynthesizer

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
    # 2. User Inputs
    # ===============================
    num_rows = st.number_input("🔢 How many synthetic rows to generate?", min_value=10, value=len(original))
    target_variable = st.text_input("🎯 Optional: What is your target variable? (Leave blank if none)")

    if st.button("🚀 Generate Synthetic Data"):
        with st.spinner("Training models... this may take a minute ⏳"):

            # ===============================
            # 3. Metadata
            # ===============================
            metadata = SingleTableMetadata()
            metadata.detect_from_dataframe(data=original)

            # ===============================
            # 4. Train Models
            # ===============================
            models = {
                "CTGAN": CTGANSynthesizer(metadata, epochs=30, verbose=False),
                "TVAE": TVAESynthesizer(metadata, enforce_min_max_values=True, enforce_rounding=True, epochs=30),
                "GaussianCopula": GaussianCopulaSynthesizer(metadata, enforce_min_max_values=True, enforce_rounding=True, default_distribution='beta'),
                "CopulaGAN": CopulaGANSynthesizer(metadata, enforce_min_max_values=True, enforce_rounding=True, epochs=30, verbose=False),
            }

            synthetic_data_dict = {}
            for name, model in models.items():
                model.fit(original)
                synthetic = model.sample(num_rows)
                synthetic_data_dict[name] = synthetic

            # ===============================
            # 5. Save to Excel
            # ===============================
            output = BytesIO()
            with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                for name, df in synthetic_data_dict.items():
                    df.to_excel(writer, sheet_name=name, index=False)
            output.seek(0)

        # ===============================
        # 6. Download Button
        # ===============================
        st.success("🎉 Synthetic datasets generated!")
        st.download_button(
            label="📥 Download Excel File with All Synthetic Datasets",
            data=output,
            file_name="synthetic_datasets.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

        # ===============================
        # 7. Optional Target Preview
        # ===============================
        if target_variable and target_variable in original.columns:
            st.subheader("🎯 Target Variable Preview")
            for name, df in synthetic_data_dict.items():
                st.markdown(f"**{name}**")
                st.dataframe(df[target_variable].value_counts())
