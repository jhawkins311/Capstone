import streamlit as st

# Page Config
st.set_page_config(page_title="Chapter 3: Workflow", layout="wide")
st.title("Chapter 3: The Process")

st.markdown("""
In this chapter, you'll walk through the full synthetic data lifecycle—from preparing your data to generating and evaluating your synthetic dataset.

Each tab below reflects a step in the workflow, based on our Google Colab interface and aligned with the SDV Library structure. All visuals and examples use the **Adult Census Income Dataset**.
""")

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["📂 Data Preparation", "🔧 Training", "🧪 Generating", "📊 Evaluating"])

# --------------------------
# 📂 Data Preparation
# --------------------------
with tab1:
    st.header("📂 Data Preparation")

    st.subheader("Install Dependencies & Import Libraries")
    st.markdown("""
Install all required Python packages and import libraries such as `pandas`, `sdv`, and `sdmetrics` to begin building the synthetic data system.
""")
    st.code("""
!pip install sdv sdmetrics plotly openpyxl XlsxWriter
import pandas as pd
from sdv.metadata import SingleTableMetadata
    """)

    st.subheader("Upload File")
    st.markdown("Upload your original dataset using an upload widget or Colab file selector.")

    st.code("""
from google.colab import files
uploaded = files.upload()
real_data = pd.read_csv("your_file.csv")
    """)

    st.subheader("Create Metadata")
    st.markdown("""
Metadata tells the synthesizer how to interpret each column. You can detect metadata automatically and visualize it.
""")
    st.code("""
metadata = SingleTableMetadata()
metadata.detect_from_dataframe(data=real_data)
metadata.visualize()
    """, language="python")

    st.image("89d973c5-70bf-4c68-82e8-327bbc5a8106.png", caption="Example: Auto-detected metadata for Adult dataset", use_column_width=True)

# --------------------------
# 🔧 Training
# --------------------------
with tab2:
    st.header("🔧 Training")

    st.markdown("""
Once metadata is created, you can initialize and train your synthesizer model (e.g., CTGAN, TVAE).

The Colab notebook defaults to **10 epochs** for fast experimentation.
""")

    st.code("""
from sdv.single_table import TVAESynthesizer
synthesizer = TVAESynthesizer(metadata)
synthesizer.fit(real_data, epochs=10)
    """, language="python")

    st.image("path_to_model_loss_plot.png", caption="TVAE Loss curve after 10 epochs", use_column_width=True)

# --------------------------
# 🧪 Generating
# --------------------------
with tab3:
    st.header("🧪 Generating")

    st.subheader("Input Sampling Details")
    st.markdown("Specify how many rows of synthetic data you want to generate.")

    st.code("""
synthetic_data = synthesizer.sample(num_rows=1000)
    """, language="python")

    st.subheader("Download Synthetic Datasets (Excel File)")
    st.markdown("Export the generated datasets using `ExcelWriter` with one tab per model.")
    st.code("""
with pd.ExcelWriter('synthetic_output.xlsx', engine='xlsxwriter') as writer:
    synthetic_data.to_excel(writer, sheet_name='TVAE', index=False)
files.download('synthetic_output.xlsx')
    """)

    st.image("path_to_scatter_plot_or_distribution.png", caption="Real vs Synthetic Feature Distributions", use_column_width=True)

# --------------------------
# 📊 Evaluating
# --------------------------
with tab4:
    st.header("📊 Evaluating")

    st.subheader("8a. Generate Evaluation Scores (Latest SDV/SDMetrics)")

    st.markdown("""
We evaluate synthetic data on three key dimensions:
- **Quality**: How well does synthetic data mimic the original?
- **Utility**: Can synthetic data be used to train downstream models?
- **Privacy**: Does the synthetic data leak personal or sensitive information?
""")

    st.code("""
from sdv.evaluation.single_table import run_diagnostic, evaluate_quality

diagnostic = run_diagnostic(real_data, synthetic_data, metadata)
quality_score = evaluate_quality(real_data, synthetic_data, metadata)
    """)

    st.image("path_to_quality_bar_chart.png", caption="Evaluation Scores (Quality & Trends)", use_column_width=True)

    st.subheader("8b. Generate Evaluation Dashboard")
    st.markdown("""
Use an interactive dashboard to compare feature distributions, privacy risk, and utility across multiple synthesizers.
""")
    st.code("""
# Dashboard code runs in Google Colab using Dash or Streamlit — see full dashboard module for details.
    """)

