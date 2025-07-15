# Streamlit Synthetic Data Evaluation Tool (Single Page Version)
# Streamlit Synthetic Data Evaluation Tool (Single Page Version)
import streamlit as st
import pandas as pd
import time

from sdv.metadata import SingleTableMetadata
from sdv.single_table import (
    CTGANSynthesizer,
    TVAESynthesizer,
    GaussianCopulaSynthesizer
)
from sdv.evaluation.single_table import evaluate_quality, run_diagnostic

# Title and Introduction
st.set_page_config(page_title="Synthetic Data Evaluation Tool")
st.title("Synthetic Data Generator & Evaluator Tool")
st.markdown("""
Welcome! This is my awesome Capstone tool for generating and evaluating synthetic data. 
""")
