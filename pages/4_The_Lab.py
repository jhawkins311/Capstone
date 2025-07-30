import streamlit as st

# Page setup
st.set_page_config(page_title="Chapter 4: The Lab", layout="wide")
st.title("Chapter 4: The Lab")

# Description
st.markdown("""
Welcome to the final chapter of **Synthetic Data 101**! 🎓

You've explored the models, workflow, and best practices for working with synthetic data. Now it's time to put that knowledge into action!


### 🧪 Launch the Lab

This is a **real synthetic data generator and evaluator** built in Google Colab. No installation needed. 

You'll upload a dataset, generate synthetic versions using four models, and receive downloadable results and evaluation charts.

If you don’t have a dataset to upload, try exploring open resources like  
[**Awesome Public Datasets**](https://github.com/awesomedata/awesome-public-datasets) or  
[**DataCamp’s Dataset Library**](https://www.datacamp.com/datalab/datasets) to get started!

**You can do this.** 💪 No coding experience required—just follow the step-by-step instructions in the notebook.

""")

# Button to simulate launching the lab
st.markdown("""
<a href="https://colab.research.google.com/drive/1HsV7spMTkvjajdbsrSqu8nIcQfE80ks0?usp=sharing" target="_blank">
    <button style='
        padding: 1.25rem 2.5rem;
        font-size: 1.25rem;
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 12px;
        font-weight: bold;
        cursor: pointer;
        margin-top: 1.5rem;
    '>
        🚀 Open the Synthetic Data Generator in Google Colab
    </button>
</a>
""", unsafe_allow_html=True)
