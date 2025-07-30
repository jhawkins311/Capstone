import streamlit as st

# Page setup
st.set_page_config(page_title="Chapter 4: The Lab", layout="wide")
st.title("Chapter 4: The Lab")

# Description
st.markdown("""
Welcome to the final chapter of **Synthetic Data 101**! 🎓

You've explored the models, workflow, and best practices for working with synthetic data. Now it's time to put that knowledge into action!


### 🧪 Launch the Lab

This is a **real synthetic data generator and evaluator** built in Google Colab. No installation needed. You'll upload a dataset, generate synthetic versions using four models, and receive downloadable results and evaluation charts.

**You can do this.** 💪 No coding experience required—just follow the step-by-step instructions in the notebook.

""")

# Button to simulate launching the lab
if st.button("🚀 Launch the Synthetic Data Lab in Google Colab"):
    st.balloons()
    st.success("🎉 Congratulations! You’ve completed the course and are ready to explore synthetic data hands-on.")

    st.markdown("""
    <div style='
        padding: 1rem;
        background-color: #e0ffe0;
        border: 2px dashed #4CAF50;
        border-radius: 12px;
        text-align: center;
        font-size: 1.2rem;
        margin-top: 1rem;
    '>
        🏅 <strong>Certified Synthetic Data Explorer</strong><br>
        You've learned the foundations, explored the tools, and now you're ready to generate privacy-safe, research-ready datasets!
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <br>
    👉 [Click here to open the Colab notebook](https://colab.research.google.com/drive/1HsV7spMTkvjajdbsrSqu8nIcQfE80ks0?usp=sharing)
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <a href="https://colab.research.google.com/drive/1HsV7spMTkvjajdbsrSqu8nIcQfE80ks0?usp=sharing" target="_blank">
        <button style='padding: 1rem 2rem; font-size: 1.25rem; background-color: #4CAF50; color: white; border: none; border-radius: 8px; cursor: pointer;'>
            🚀 Open the Synthetic Data Generator in Google Colab
        </button>
    </a>
    """, unsafe_allow_html=True)


