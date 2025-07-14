import streamlit as st
from sdv.evaluation.single_table import evaluate_quality, run_diagnostic

st.title("📊 Evaluate & Compare Synthetic Data")

required_keys = ["df", "metadata", "synthetic_ctgan", "synthetic_tvae", "synthetic_gaussian"]

if not all(k in st.session_state for k in required_keys):
    st.warning("Please generate synthetic data first.")
    st.stop()

df = st.session_state["df"]
metadata = st.session_state["metadata"]
sensitive_cols = st.session_state.get("sensitive_cols", [])
target_col = st.session_state.get("target_col", None)

for name, synth_df in [
    ("CTGAN", st.session_state["synthetic_ctgan"]),
    ("TVAE", st.session_state["synthetic_tvae"]),
    ("Gaussian Copula", st.session_state["synthetic_gaussian"])
]:
    st.header(f"{name} Evaluation")

    diagnostic = run_diagnostic(real_data=df, synthetic_data=synth_df, metadata=metadata)
    quality = evaluate_quality(real_data=df, synthetic_data=synth_df, metadata=metadata)

    st.subheader("Diagnostic Report")
    st.json(diagnostic.get_results())

    st.subheader("Quality Report")
    st.json(quality.get_results())

    if sensitive_cols:
        st.subheader("Privacy Metrics (column shape risks)")
        risks = {col: quality.get_details(property_name="Column Shapes", column_name=col) for col in sensitive_cols}
        st.json(risks)

    if target_col:
        st.subheader("ML Utility Metric (target column shape)")
        utility = quality.get_details(property_name="Column Shapes", column_name=target_col)
        st.json({target_col: utility})

    st.subheader("Sample Comparison")
    st.write("Real Data")
    st.dataframe(df.head(10))
    st.write(f"Synthetic Data ({name})")
    st.dataframe(synth_df.head(10))
