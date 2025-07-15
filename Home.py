# Home Page

# Import Streamlit
import streamlit as st

# Page Configuration & Titles
st.set_page_config(page_title="Synthetic Data 101")

st.title("A Beginner's Guide to Synthetic Data")

# Text for Homepage - Explains the "course" structure" 
st.markdown("""

Welcome to Synthetic Data 101! 

This is a free and open-source tool to explore, compare, and generate synthetic datasets for privacy-compliant machine learning and education.

### For this course, just follow the tabs in the sidebar:
1. **How do we make it?** – Learn about the different systhetic data models and when to use them
2. **What does it look like?** – See how each model performs on real datasets
3. **Can I try it?** – Upload your own dataset, generate multiple synthetic datasets, and view the resutling evaluation dashboard

### If you would like to learn more about synthetic data or working on a related research project, please watch our tool development video: 
[Hyperlink to the final capstone presentation]


❤️ This webapp was deeigned with love for students, data analysts, professional who want to try synthetic data tools before investing in expensive platforms ❤️
""")
