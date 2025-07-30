import streamlit as st

#Page Layout & Titles
st.set_page_config(page_title="SDV Libraries")

st.title("Synthetic Data Vault Libraries")

# Page Content - SDV Libaries
st.markdown("""

Welcome to **Module 1** of our Synthetic Data 101 course!  

Here, you'll explore basic table synthesizers. These models specialize in processing a single table of data and outputting a synethetic verision. 

### A Quick Guide on SDV Libraries

| Generative Model   | Type of Data           | Strengths                                           | Limitations                    | Speed                   |
|--------------------|------------------------|-----------------------------------------------------|--------------------------------|-------------------------|
| **CTGAN**          | Numerical, Categorical | Great for mixed-type data, imbalanced columns       | Requires tuning                | Slow                    |      
| **TVAE**           | Numerical, Categorical | Used for complex data with non-linear relationships | Slightly more complex          | Medium                  |     
| **GaussianCopula** | Mostly Numerical       | Fast & easy to use                                  | Uses statistical estimates     | Fast                    |    


The main three generative models from the **[Synthetic Data Vault (SDV)](https://docs.sdv.dev/)** library are: 

### (1) CTGAN
The CTGAN Synthesizer uses GAN-based methods to learn from real data. 
GAN refers to Generative Adversarial Network. It's a type of neural network architecture where two networks, a generator and a discriminator, compete to improve each other. 
The generator creates new data instances, while the discriminator tries to identify whether the data is real (from the training set) or generated. 
This adversarial process leads to the generator producing increasingly realistic data. 

It is the benchmark library used to produce synthetic data with high fidelity! However, it takes the longest. 

### (2) TVAE
The TVAE Synthesizer uses a variational autoencoder (VAE)-based, neural network techniques to learn from real data. It has a medium speed and increased quality, but it takes longer to learn.

### (3) GaussianCopula
The Gaussian Copula Synthesizer uses classic statistiical ML methods to learn from real data. It is fast and produces quality results, but it specializes on numerical-only datasets. 


""")
