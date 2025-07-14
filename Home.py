# Streamlit Synthetic Data Evaluation Tool (Single Page Version)
# Streamlit Synthetic Data Evaluation Tool (Single Page Version)
import streamlit as st
import pandas as pd
import time

from sdv.metadata import SingleTableMetadata
from sdv.single_table import (
    CTGANSynthesizer,
    TVAESynthesizer,
    GaussianCopulaSynthesizer
)
from sdv.evaluation.single_table import evaluate_quality, run_diagnostic

# Title and Introduction
st.set_page_config(page_title="Synthetic Data Evaluation Tool")
st.title("🧪 Synthetic Data Evaluation Tool")
st.markdown("""
Welcome! This tool allows novice data analysts to generate and evaluate synthetic datasets
using generative AI models like CTGAN, TVAE, and Gaussian Copula.
Upload your tabular data, define sensitive and target columns, and view diagnostics, quality, and ML utility metrics.
""")

# Upload File
uploaded_file = st.file_uploader("📂 Upload your CSV dataset", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("## 📄 Dataset Preview")
    st.dataframe(df.head(10))

    # Column Selection
    columns = df.columns.tolist()
    sensitive_cols = st.multiselect("🔐 Select sensitive columns (for privacy)", columns)
    target_col = st.selectbox("🎯 Select a target column (for ML utility evaluation, optional)", [None] + columns)

    # Metadata
    metadata = SingleTableMetadata()
    metadata.detect_from_dataframe(data=df)
    st.write("## 🧬 Detected Metadata")
    st.json(metadata.to_dict())

    # Button to Generate
    if st.button("🚀 Generate & Evaluate Synthetic Data"):
        model_options = [
            ("CTGAN", CTGANSynthesizer(metadata, epochs=50, verbose=True)),
            ("TVAE", TVAESynthesizer(metadata, epochs=50, verbose=True)),
            ("Gaussian Copula", GaussianCopulaSynthesizer(metadata))
        ]

        for name, synthesizer in model_options:
            st.subheader(f"🔄 Training {name}...")
            with st.spinner(f"Training {name}... this may take a moment"):
                synthesizer.fit(df)
                synthetic_df = synthesizer.sample(len(df))
            st.success(f"✅ {name} synthetic data generated!")

            # Run diagnostics and quality
            st.info("Evaluating synthetic data...")
            with st.spinner("Running diagnostics and quality metrics..."):
                diagnostic = run_diagnostic(real_data=df, synthetic_data=synthetic_df, metadata=metadata)
                quality = evaluate_quality(real_data=df, synthetic_data=synthetic_df, metadata=metadata)
            st.success("📈 Evaluation complete!")

            st.write(f"### 🧪 {name} - Diagnostic Report")
            st.json(diagnostic.get_results())

            st.write(f"### 📊 {name} - Quality Report")
            st.json(quality.get_results())

            if sensitive_cols:
                st.write(f"### 🔍 {name} - Privacy Metric Highlights")
                disclosure_risks = {}
                for col in sensitive_cols:
                    try:
                        risk = quality.get_details(property_name="Column Shapes", column_name=col)
                        disclosure_risks[col] = risk
                    except Exception as e:
                        disclosure_risks[col] = str(e)
                st.write(disclosure_risks)

            if target_col:
                st.write(f"### 🎓 {name} - ML Utility Score for {target_col}")
                try:
                    ml_utility = quality.get_details(property_name="Column Shapes", column_name=target_col)
                    st.write({target_col: ml_utility})
                except Exception as e:
                    st.warning(f"Could not evaluate ML utility: {e}")

            # Sample comparison
            st.write("### 🧾 Sample Data Comparison")
            st.write("Real Data:")
            st.dataframe(df.head(5))
            st.write(f"Synthetic Data from {name}:")
            st.dataframe(synthetic_df.head(5))

else:
    st.warning("Please upload a CSV file to begin.")
