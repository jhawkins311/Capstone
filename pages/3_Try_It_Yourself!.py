# Streamlit Synthetic Data Evaluation Tool – Try It Yourself Page
import streamlit as st
import pandas as pd
import datetime
import uuid

# Page config
st.set_page_config(page_title="Try It Yourself!")
st.title("Try It Yourself!")

st.markdown("""
Upload your dataset! 

This tool will generate synthetic datasets using three models (CTGAN, TVAE, Gaussian Copula) in the cloud. 
**Note:** Processing can take 5–15 minutes. 

You'll receive a unique Job ID to retrieve your results later.
**Note:** Please remember to save your Job ID!

""")

# Upload
uploaded_file = st.file_uploader("Upload your CSV dataset", type=["csv"])

# Email input (optional)
email = st.text_input("Enter your email to receive all the results (optional)")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### Uploaded Data")
    st.write(df.head())

    # Generate a unique job ID and save temp file
    job_id = uuid.uuid4().hex[:8] + datetime.datetime.now().strftime("_%Y%m%d_%H%M%S")
    filename = f"data_{job_id}.csv"
    df.to_csv(filename, index=False)

    st.success(f"✅ File saved as `{filename}` with Job ID: `{job_id}`")

    st.markdown("""
    ### ✅ Next Step:
    [Open Google Colab to process your data ➜](https://colab.research.google.com/drive/1cR4EzXeVVAnrY9-Qw_K1k6v2sQSy78N6?usp=sharing)
    
    When prompted, upload the saved CSV file above.
    
    The notebook will train all 3 models, evaluate the synthetic datasets, and generate a downloadable ZIP.
    """)

st.markdown("---")
st.header("Getting the Results")

st.markdown("""
If you have already run the Colab notebook and have a Job ID, enter it below to download your results.
""")

job_input = st.text_input("Enter your Job ID")

if job_input:
    # Create shared URL template
    base_url = "https://drive.google.com/uc?export=download&id="
    file_id_mapping = {
        # Example mapping – must be populated manually or via Google Drive API integration
        "demo_20250715_1015": "1XxYyZzAABBCCDDEEFFGGHHIIJJ"  # Replace with real ID
    }

    if job_input in file_id_mapping:
        gdrive_id = file_id_mapping[job_input]
        download_url = base_url + gdrive_id
        st.markdown(f"[🔽 Download Results for `{job_input}`]({download_url})")
    else:
        st.warning("No results found for this Job ID. Please verify spelling or try again later.")
