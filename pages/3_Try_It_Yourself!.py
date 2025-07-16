# Page 3 - Try It Yourself (Colab Backend)
import streamlit as st
import pandas as pd
import requests
import time

# Page Setup
st.set_page_config(page_title="Try It Yourself - Synthetic Data Tool")
st.title("Try It Yourself")

st.markdown("""
### Upload your own dataset and generate synthetic versions with CTGAN, TVAE, and GaussianCopula models.
This uses Google Colab as a backend to avoid timeouts.

Results may take a few minutes. 

You’ll receive a Job ID to check your results later.
Remember your Job ID!

When processing is done, your results will be available as a downloadable .zip file.
""")

st.markdown("---")

# File Upload Section
uploaded_file = st.file_uploader("Upload your CSV dataset", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("✅ File uploaded successfully!")
    st.write("### Data Preview")
    st.dataframe(df.head())

    # Input a job name
    job_id = st.text_input("Enter a Job ID (e.g. your initials + date):", max_chars=20)

    if st.button("🚀 Submit to Google Colab for Processing"):
        st.write("🔄 Uploading and sending to Colab...")

        # Save to disk for upload
        with open("input_dataset.csv", "wb") as f:
            f.write(uploaded_file.getvalue())

        # Simulated message while user runs Colab manually
        st.success(f"Your Job ID is **{job_id}**. Please open the Colab Notebook to complete processing:")
        st.markdown("[🔗 Open Google Colab Notebook](https://colab.research.google.com/drive/1RANDOMCOLABID)")
        st.markdown("Once the Colab script completes, return here to download your results.")

st.markdown("---")

st.header("📥 Retrieve Results")
st.markdown("Enter your Job ID to get your synthetic data evaluation results.")

# Google Drive Result Link Builder
job_to_id = {
    # Pre-populate this manually for each job
    "test123": "1AbCdEfGHiJKLMNOPQRSTUVWXYZ",  # Job ID -> File ID
    # Add more mappings here
}

result_job_id = st.text_input("Enter your Job ID to retrieve results:")

if st.button("🔍 Get Results") and result_job_id:
    file_id = job_to_id.get(result_job_id)

    if file_id:
        download_url = f"https://drive.google.com/uc?id={file_id}&export=download"
        st.success("✅ Results Found!")
        st.markdown(f"[📦 Click to Download Results ZIP](https://drive.google.com/uc?id={file_id}&export=download)")
        st.image("sample_preview.png", caption="Sample Visualization", use_column_width=True)
    else:
        st.error("❌ No results found for that Job ID. Please double-check or try again later.")

st.markdown("---")
st.caption("Note: Results are sessionless and not saved by the server. Your uploaded file is not stored.")
