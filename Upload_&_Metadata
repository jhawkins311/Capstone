import streamlit as st
import pandas as pd
from sdv.metadata import SingleTableMetadata

st.title("📤 Upload Your Dataset")

# File upload
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.session_state["df"] = df

    st.write("### Dataset Preview")
    st.dataframe(df.head())

    # Metadata detection
    metadata = SingleTableMetadata()
    metadata.detect_from_dataframe(data=df)
    st.session_state["metadata"] = metadata

    st.write("### Metadata")
    st.json(metadata.to_dict())

    # Column selection
    columns = df.columns.tolist()
    sensitive = st.multiselect("Select sensitive columns (for privacy)", columns)
    target = st.selectbox("Select target column (for ML evaluation)", [None] + columns)

    st.session_state["sensitive_cols"] = sensitive
    st.session_state["target_col"] = target
