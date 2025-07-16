import streamlit as st
from PIL import Image

st.title("Example: Adult Dataset Results")

tabs = st.tabs(["Uploading", "Modeling", "Generating", "Evaluating"])

with tabs[0]:
    st.header("Uploading an Original Dataset")
    st.image("assets/adult_metadata.png", caption="Metadata Visualization")
    st.dataframe(pd.read_csv("assets/adult_real_preview.csv").head())

with tabs[1]:
    st.header("Creating Generative AI Models")
    st.markdown("We used CTGAN, TVAE, and GaussianCopula with default SDV parameters.")
    st.code("""
ctgan = CTGANSynthesizer(metadata)
ctgan.fit(real_data)
synthetic_data = ctgan.sample(num_rows)
""")

with tabs[2]:
    st.header("Generating Synthetic Datasets")
    st.dataframe(pd.read_csv("assets/adult_synthetic_ctgan.csv").head())

with tabs[3]:
    st.header("Evaluating Synthetic Datasets")
    st.image("assets/adult_quality_report.png", caption="Quality Score Comparison")
    st.image("assets/adult_loss_plot.png", caption="Loss Plot During Training")
