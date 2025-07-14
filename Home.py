# Streamlit Synthetic Data Evaluation Tool (Single Page Version)
import streamlit as st
import pandas as pd
from sdv.metadata import SingleTableMetadata
from sdv.single_table import CTGANSynthesizer
from sdv.evaluation.single_table import evaluate_quality, run_diagnostic

# Title and Description
st.title("🧪 Synthetic Data Generator & Evaluator")
st.markdown("""
Welcome! This tool lets you upload your own tabular dataset, generate synthetic data using **CTGAN**, and evaluate the results.
Ideal for privacy-compliant ML training and teaching.
""")

# Upload CSV File
uploaded_file = st.file_uploader("📁 Upload your CSV dataset", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### 🔍 Dataset Preview")
    st.dataframe(df.head())

    # Column Selection
    columns = df.columns.tolist()
    sensitive_cols = st.multiselect("🔒 Select sensitive columns (optional)", columns)
    target_col = st.selectbox("🎯 Select a target column (for ML evaluation, optional)", [None] + columns)

    # Detect metadata
    metadata = SingleTableMetadata()
    metadata.detect_from_dataframe(data=df)
    st.write("### 📊 Detected Metadata")
    st.json(metadata.to_dict())

    if st.progress("🚀 Generate & Evaluate Synthetic Data"):
        with st.progress("Training CTGAN... this may take a few moments"):
            synthesizer = CTGANSynthesizer(metadata, epochs=300, verbose=True)
            synthesizer.fit(df)
            synthetic_df = synthesizer.sample(len(df))

        st.success("Synthetic data generated successfully!")

        # Run Evaluation
        with st.progress("Running diagnostic and quality reports..."):
            diagnostic = run_diagnostic(real_data=df, synthetic_data=synthetic_df, metadata=metadata)
            quality = evaluate_quality(real_data=df, synthetic_data=synthetic_df, metadata=metadata)

        st.write("## ✅ Evaluation Results")

        st.write("### 🔬 Diagnostic Report")
        st.json(diagnostic.get_results())

        st.write("### 📈 Quality Report")
        st.json(quality.get_results())

        if sensitive_cols:
            st.write("### 🛡️ Privacy Metrics")
            risks = {col: quality.get_details("Column Shapes", col) for col in sensitive_cols}
            st.json(risks)

        if target_col:
            st.write("### 🤖 ML Utility Metrics")
            target_eval = quality.get_details("Column Shapes", target_col)
            st.json({target_col: target_eval})

        st.write("### 📄 Data Comparison")
        st.write("**Real Data (First 10 rows):**")
        st.dataframe(df.head(10))

        st.write("**Synthetic Data (First 10 rows):**")
        st.dataframe(synthetic_df.head(10))

else:
    st.info("Please upload a CSV file to begin.")
