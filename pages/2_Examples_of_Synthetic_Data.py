import streamlit as st
from sdv.single_table import (
    CTGANSynthesizer,
    TVAESynthesizer,
    GaussianCopulaSynthesizer
)
from sdv.evaluation.single_table import evaluate_quality, run_diagnostic

st.title("Step 2: Generate and Evaluate Synthetic Data")

if "df" not in st.session_state or "metadata" not in st.session_state:
    st.warning("Please upload a dataset and generate metadata first.")
    st.stop()

# Column Selection
df = st.session_state["df"]
metadata = st.session_state["metadata"]

columns = df.columns.tolist()
sensitive_cols = st.multiselect("Select sensitive columns (for privacy)", columns)
target_col = st.selectbox("Select a target column (for ML evaluation, optional)", [None] + columns)

model_choice = st.selectbox("Select a synthesizer to train:", ["CTGAN", "TVAE", "Gaussian Copula"])

if st.button("Train and Evaluate"):
    with st.spinner(f"Training {model_choice} model..."):
        if model_choice == "CTGAN":
            synthesizer = CTGANSynthesizer(metadata, epochs=300, verbose=True)
        elif model_choice == "TVAE":
            synthesizer = TVAESynthesizer(metadata, epochs=300, verbose=True)
        else:
            synthesizer = GaussianCopulaSynthesizer(metadata)

        synthesizer.fit(df)
        synthetic_data = synthesizer.sample(len(df))

        diagnostic = run_diagnostic(real_data=df, synthetic_data=synthetic_data, metadata=metadata)
        quality = evaluate_quality(real_data=df, synthetic_data=synthetic_data, metadata=metadata)

        # Save to session state
        st.session_state[f"{model_choice}_diagnostic"] = diagnostic
        st.session_state[f"{model_choice}_quality"] = quality
        st.session_state[f"{model_choice}_synthetic"] = synthetic_data

        st.success(f"{model_choice} model trained and evaluated!")

        # Display Results
        st.subheader("Quality Report")
        st.write(quality.get_results())

        st.subheader("Diagnostic Report")
        st.write(diagnostic.get_results())

        if sensitive_cols:
            st.subheader("Privacy Metrics")
            privacy_scores = {}
            for col in sensitive_cols:
                privacy_scores[col] = quality.get_details(property_name="Column Shapes", column_name=col)
            st.write(privacy_scores)

        if target_col:
            st.subheader("ML Utility Metrics")
            ml_score = quality.get_details(property_name="Column Shapes", column_name=target_col)
            st.write({target_col: ml_score})

        st.subheader("Synthetic vs Real Data Sample")
        st.write("Real Data:")
        st.write(df.head(10))
        st.write("Synthetic Data:")
        st.write(synthetic_data.head(10))

        csv = synthetic_data.to_csv(index=False).encode()
        st.download_button(
            label=f"Download Synthetic Data ({model_choice})",
            data=csv,
            file_name=f"{model_choice}_synthetic.csv",
            mime="text/csv"
        )
