# Home Page

# Import Streamlit
import streamlit as st

# Page Configuration & Titles
st.set_page_config(page_title="Synthetic Data 101")

st.title("A Beginner's Guide to Synthetic Data")

# Text for Homepage - Explains the "course" structure" 
st.markdown("""

Welcome to Synthetic Data 101! 

In this interactive course, you will explore Python libraries, examine synthetic datasets, and experiment with making your own synthetic datasets for privacy-compliant machine learning and education.

### Just follow the tabs in the sidebar:
1. **Synthetic Data Vault Libraries** - Learn about the different systhetic data generation models and when to use each
2. **Examples of Synthetic Data** – See how each model performs on real datasets
3. **Try It Yourself!** – Upload your own dataset, generate synthetic versions using multiple libraries, and view the resutling evaluation dashboard

### If you would like to learn more about synthetic data or working on a related research project, please watch our tool development video: 
[Hyperlink to the final capstone presentation]


❤️ This webapp was deeigned with love for students, data analysts, professional who want to try synthetic data tools before investing in expensive platforms ❤️
""")
