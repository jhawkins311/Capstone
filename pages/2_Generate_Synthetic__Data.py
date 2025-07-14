import streamlit as st
from sdv.single_table import CTGANSynthesizer, TVAESynthesizer, GaussianCopulaSynthesizer

st.title("🤖 Generate Synthetic Data")

# Check if data is loaded
if "df" not in st.session_state or "metadata" not in st.session_state:
    st.warning("Please upload a dataset first on the 'Upload & Metadata' page.")
    st.stop()

df = st.session_state["df"]
metadata = st.session_state["metadata"]

if st.button("Generate Data"):
    with st.spinner("Training models..."):

        ctgan = CTGANSynthesizer(metadata, epochs=300, verbose=True)
        ctgan.fit(df)
        synthetic_ctgan = ctgan.sample(len(df))
        st.session_state["synthetic_ctgan"] = synthetic_ctgan

        tvae = TVAESynthesizer(metadata, epochs=300, verbose=True)
        tvae.fit(df)
        synthetic_tvae = tvae.sample(len(df))
        st.session_state["synthetic_tvae"] = synthetic_tvae

        gaussian = GaussianCopulaSynthesizer(metadata)
        gaussian.fit(df)
        synthetic_gaussian = gaussian.sample(len(df))
        st.session_state["synthetic_gaussian"] = synthetic_gaussian

    st.success("Synthetic data generated!")
