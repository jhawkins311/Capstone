# Home Page

# Import Streamlit
import streamlit as st

# Page Configuration & Titles
st.set_page_config(page_title="Synthetic Data 101", layout="wide")

st.title("A Beginner's Guide to Synthetic Data")

# Text for Homepage - Explains the "course" structure" 
st.markdown("""

Welcome to Synthetic Data 101, an interactive course designed for students, data analysts, professionals eager to explore the world of synthetic data!

Throughout this guided experience, you'll learn how synthetic data can be generated, evaluated, and applied—all without writing a single line of code. Whether you're new to the concept or looking to sharpen your skills, this course will walk you through the tools and techniques used by today’s data scientists and privacy engineers.

---

### 📚 Course Chapters

#### **Chapter 1: The History**
Discover how synthetic data came to be, the problems it solves, and why it’s increasingly essential in modern AI and analytics workflows.

#### **Chapter 2: The Models**
Meet the four core models used to generate synthetic datasets: CTGAN, TVAE, GaussianCopula, and CopulaGAN. Learn what makes each model unique—and when to use them.

#### **Chapter 3: The Process**
Follow a simple, structured process to upload your dataset, train generative models, sample synthetic data, and evaluate the results—all within your browser.

#### **Chapter 4: The Lab**
Put your knowledge into practice using our interactive Google Colab lab. Generate your own synthetic datasets and run advanced evaluation metrics with just a few clicks.

---

### If you would like to learn how this tool was developed, please check out the full research project: 
[COMING SOON: Hyperlink to the final capstone presentation]


❤️ This webapp was designed with love for those who want to try synthetic data tools before investing in expensive platforms ❤️
""")
