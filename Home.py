# Home Page

# Import Streamlit
import streamlit as st

# Page Configuration & Titles
st.set_page_config(page_title="Synthetic Data 101", layout="wide")

st.title("Synthetic Data 101")

# Text for Homepage - Explains the "course" structure" 
st.markdown("""

Welcome to the world of synthetic data! 

Throughout this interactive course, you'll learn about why synethetic data is important, what methods are used to generate it, and how it can be evaluated for reliablity. 

---

### 📚 Course Chapters

#### [**Chapter 1: The History**](https://capstone-dz3iduiobkviwaijgqcvqg.streamlit.app/The_History)
Discover how the need for privacy-preservation lead to the creation of synthetic data and why it's essential for modern AI tools

#### [**Chapter 2: The Models**](https://capstone-dz3iduiobkviwaijgqcvqg.streamlit.app/The_Models)
Meet the four core models used to generate synthetic datasets: CTGAN, TVAE, GaussianCopula, and CopulaGAN, 

#### [**Chapter 3: The Process**](https://capstone-dz3iduiobkviwaijgqcvqg.streamlit.app/The_Process)
See a full example of the synthetic data process in action, from uploading a dataset to evaluating the results. 

#### [**Chapter 4: The Lab**](https://capstone-dz3iduiobkviwaijgqcvqg.streamlit.app/The_Lab)
Put your knowledge into practice by using our interactive Google CoLAB. Generate multiple synthetic datasets and evaluate them in just a few clicks! 

---

### If you would like to learn how this tool was developed, please check out the full research project: 

[COMING SOON: Hyperlink to the final capstone presentation]


❤️ This webapp was designed with love for students, professionals, and developers who want to explore free synthetic data tools before investing in expensive platforms ❤️
""")
