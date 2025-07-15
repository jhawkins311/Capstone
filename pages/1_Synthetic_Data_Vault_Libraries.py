import streamlit as st

#Page Layout & Titles
st.set_page_config(page_title="SDV Libraries")

st.title("Synthetic Data Vault Libraries")

# Page Content - SDV Libaries
st.markdown("""

Welcome to **Module 1** of our Synthetic Data 101 course!  

Here, you'll explore three generative models from the **[Synthetic Data Vault (SDV)](https://docs.sdv.dev/)** library: 

### (1) CTGAN - "The CTGAN Synthesizer uses GAN-based, deep learning methods to learn from real data. It is the benchmark library used to produce synthetic data with high fidelity. However, it takes the longest. 

### (2) TVAE - The TVAE Synthesizer uses a variational autoencoder (VAE)-based, neural network techniques to learn from real data. It has a medium speed and increased quality, but it takes longer to learn.

### (3) GaussianCopula - The Gaussian Copula Synthesizer uses classic statistiical ML methods to learn from real data. It is fast and produces quality results, but it specializes on numerical-only datasets. 


These models are basic table synthesizers. This means the model can process a single table of data and output a synethetic verision. 


### A quick guide for each model

| Generative Model   | Type of Data           | Strengths                                           | Limitations                    | Speed                   |
|--------------------|------------------------|-----------------------------------------------------|--------------------------------|-------------------------|
| **CTGAN**          | Numerical, Categorical | Great for mixed-type data, imbalanced columns       | Requires tuning                | Slow                    |      
| **TVAE**           | Numerical, Categorical | Used for complex data with non-linear relationships | Slightly more complex          | Medium                  |     
| **GaussianCopula** | Mostly Numerical         | Fast & easy to use                                  | Uses statistical estimates   | Fast                    |    

""")
