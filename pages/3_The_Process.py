import streamlit as st

# Page Configuration
st.set_page_config(page_title="Chapter 3: The Process", layout="wide")
st.title("Chapter 3: The Process 🧭")

# Intro Text
st.markdown("""
Welcome to Chapter 3: Workflow of the Synthetic Data 101 course!

This chapter walks you through the **entire synthetic data generation lifecycle**, based on the structure of our **Google Colab Lab Notebook**. 

---

### The Lifecycle of Synthetic Data

Now that you’ve learned about the models, it’s time to walk through the complete process of generating synthetic data.

Each tab represents a key stage of the process—from data preparation to results evaluation. Follow the visuals and code snippets from our example tests on the **Adult Census Dataset**.

> ⚠️ *This page is a walkthrough only. For real execution, please visit the Lab in Chapter 4.*
""")

# Tabs based on notebook phases
tab1, tab2, tab3, tab4 = st.tabs([
    "📂 Data Preparation",
    "⚙️ Training",
    "🧪 Generating",
    "📊 Evaluating"
])

# ---------------------------------------
# Tab 1: Data Preparation
# ---------------------------------------
with tab1:
    st.header("📂 Data Preparation")

    st.markdown("""
Before training a synthesizer, you'll need to load your data and generate its metadata.

### Steps in the Lab Notebook:
1. **Install Dependencies** – Required Python packages (SDV, Pandas, Plotly, etc.)
2. **Import Libraries** – Essential modules and functions
3. **Upload File** – Upload a `.csv` file using the notebook’s interface
4. **Create Metadata** – Automatically detect column types using SDV

### Example Code:
    """)
    st.code("""
from sdv.metadata import SingleTableMetadata

metadata = SingleTableMetadata()
metadata.detect_from_dataframe(data=real_data)
metadata.visualize()
    """, language="python")

    st.image("https://raw.githubusercontent.com/your-username/your-repo/main/images/metadata_preview.png", 
             caption="Metadata detected from Adult dataset", 
             use_column_width=True)

# ---------------------------------------
# Tab 2: Training
# ---------------------------------------
with tab2:
    st.header("⚙️ Training")

    st.markdown("""
Once the metadata is prepared, you'll train four synthesizer models on your dataset:
- CTGAN
- TVAE
- GaussianCopula
- CopulaGAN

The notebook uses 10 training epochs per model for speed and comparison.

### Example: TVAE Model
    """)
    st.code("""
from sdv.single_table import TVAESynthesizer

synthesizer = TVAESynthesizer(
    metadata=metadata,
    enforce_rounding=False,
    epochs=10,
    verbose=True
)

synthesizer.fit(real_data)
    """, language="python")

    st.image("https://raw.githubusercontent.com/your-username/your-repo/main/images/loss_plot_tvae.png", 
             caption="Training loss plot for TVAE on Adult dataset", 
             use_column_width=True)

# ---------------------------------------
# Tab 3: Generating
# ---------------------------------------
with tab3:
    st.header("🧪 Generating")

    st.markdown("""
After training, you’ll generate synthetic data using each model. You’ll also be prompted to enter how many rows to sample.

The results are saved into an Excel file with **separate tabs for each model’s output**.

### Sampling Code Example:
    """)
    st.code("""
synthetic_data = synthesizer.sample(num_rows=1000)
    """, language="python")

    st.image("https://raw.githubusercontent.com/your-username/your-repo/main/images/sample_distribution.png", 
             caption="Real vs Synthetic distributions on Adult dataset", 
             use_column_width=True)

# ---------------------------------------
# Tab 4: Evaluating
# ---------------------------------------
with tab4:
    st.header("📊 Evaluating")

    st.markdown("""
The final step is to evaluate the synthetic datasets based on:
- **Quality** – Distribution similarity
- **Utility** – Model compatibility
- **Privacy** – Disclosure and overfitting risk

The Lab generates both a summary table and an interactive dashboard.

### Example Evaluation Code:
    """)
    st.code("""
from sdv.evaluation.single_table import evaluate_quality, run_diagnostic

diagnostic = run_diagnostic(real_data, synthetic_data, metadata)
quality_score = evaluate_quality(real_data, synthetic_data, metadata)
    """, language="python")

    st.image("https://raw.githubusercontent.com/your-username/your-repo/main/images/eval_scores.png", 
             caption="Evaluation results showing quality and trend scores", 
             use_column_width=True)

    st.markdown("""
👉 Full column-level visualizations and privacy reports are available inside the Lab in **Chapter 4**.
""")


# Final Navigation Tip
st.markdown("""
---

### Next Up: The Lab 🧪

Now that you have seen how analysts generate and evaluate synthetic data, now you can try!
""")
