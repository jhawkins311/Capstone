import streamlit as st

# Page Layout & Title
st.set_page_config(page_title="Chapter 2: Models", layout="wide")
st.title("Chapter 2: The Models ⚙️")

# Page Description
st.markdown("""
Welcome to the synthetic data models library!

In this chapter, you'll explore four foundational models from the [Synthetic Data Vault (SDV)](https://docs.sdv.dev/). 

""")

# Synthesizer Comparison Table
st.markdown("""
---

### Basic Single Table Synthesizers

**Synthesizers** are tools that use machine learning algorithms that:
1) Learn the patterns and characteristics from real datasets
3) Create artificial data that maintains the same statistical characteristics and behavior as the original
""")

# Tabs for each model
ctgan_tab, tvae_tab, gc_tab, copulagan_tab = st.tabs(["CTGAN", "TVAE", "GaussianCopula", "CopulaGAN"])

# --- CTGAN Tab ---
with ctgan_tab:
    st.subheader("CTGAN — Conditional Tabular Generative Adversarial Network")

    st.markdown("""
The **CTGAN Synthesizer** uses a GAN-based approach where a generator and discriminator compete to improve output quality.  

It’s particularly effective on **imbalanced** and **mixed-type** datasets (e.g., medical or credit data).  

CTGAN can take longer to train but often produces high-fidelity results that preserve deep feature relationships.

>**Best for:** High-stakes, highly structured datasets where accuracy matters most.

""")

    with st.expander("Show CTGAN Example Code"):
        st.code("""
# Create the CTGAN Model
from sdv.single_table import CTGANSynthesizer

# The CTGAN model trains on the metadata to learn the data's structure (ex: what the synthetic dataset should look like) 
# The metadata describes the structure of the data (column types, constraints, etc.)
CTGAN_synthesizer = CTGANSynthesizer(
    metadata,        
    enforce_rounding=False,
    epochs=300,
    verbose=True
)

# The CTGAN model trains on the original dataset to learn pattern and relationships (ex: what the synthetic dataset should contain)
CTGAN_synthesizer.fit(real_data)

# A 1,000 row synthetic dataset is generated from the CTGAN model
ctgan_synthetic_data = CTGAN_synthesizer.sample(num_rows=1000)
        """, language="python")

# --- TVAE Tab ---
with tvae_tab:
    st.subheader("TVAE — Tabular Variational Autoencoder")

    st.markdown("""
The **TVAE Synthesizer** relies on **variational autoencoders** (VAEs), which compress and reconstruct the dataset to learn its structure.  

This makes it great for capturing **non-linear patterns** in data—like complex interactions between features.

> **Best for:** Mid-size datasets where relationships between variables are important.
""")

    with st.expander("Show TVAE Example Code"):
        st.code("""
# Create the TVAE Model        
from sdv.single_table import TVAESynthesizer

# The TVAE model trains on the metadata to learn the data's structure (ex: what the synthetic dataset should look like) 
# The metadata describes the structure of the data (column types, constraints, etc.)
synthesizer = TVAESynthesizer(
    metadata,           
    enforce_rounding=False,
    epochs=300,
    verbose=True
)

# The TVAE model trains on the original dataset to learn pattern and relationships (ex: what the synthetic dataset should contain)
synthesizer.fit(real_data)

# A 1,000 row synthetic dataset is generated from the TVAE model
synthetic_data = synthesizer.sample(num_rows=1000)
        """, language="python")

# --- GaussianCopula Tab ---
with gc_tab:
    st.subheader("GaussianCopula — Copula of a d-dimensional Gaussian random variable")

    st.markdown("""
The **GaussianCopula Synthesizer** is the simplest of the four.  

It uses classic statistical transformations to model relationships, assuming a multivariate normal structure.  

While limited to mostly numerical data, it’s **very fast** and **easy to use**, making it ideal for prototyping or educational use.

> **Best for:** Quick generation of synthetic data when speed or simplicity is a priority.
""")

    with st.expander("Show GaussianCopula Example Code"):
        st.code("""
# Create the GaussianCopula Model
from sdv.single_table import GaussianCopulaSynthesizer

# The GaussianCopula model trains on the metadata to learn the data's structure (ex: what the synthetic dataset should look like) 
# The metadata describes the structure of the data (column types, constraints, etc.)
synthesizer = GaussianCopulaSynthesizer(metadata)

# The GaussianCopula model trains on the original dataset to learn pattern and relationships (ex: what the synthetic dataset should contain)
synthesizer.fit(real_data)

# A 1,000 row synthetic dataset is generated from the GaussianCopula model
synthetic_data = synthesizer.sample(num_rows=1000)
        """, language="python")

# --- CopulaGAN Tab ---
with copulagan_tab:
    st.subheader("CopulaGAN — Generative Adversarial Networks (GANs) with Copulas")

    st.markdown("""
The **CopulaGAN Synthesizer** is a **hybrid model** that blends GANs with statistical copulas.  

It offers a middle ground between deep learning complexity and traditional modeling, aiming to balance **accuracy**, **privacy**, and **speed**.

> **Best for:** Scenarios that demand both performance and speed, such as limited-resource environments or pilot testing.
""")

    with st.expander("Show CopulaGAN Example Code"):
        st.code("""
# Create the CopulaGAN Model
from sdv.single_table import CopulaGANSynthesizer

# The CopulaGAN model trains on the metadata to learn the data's structure (ex: what the synthetic dataset should look like) 
synthesizer = CopulaGANSynthesizer(
    metadata,
    enforce_rounding=False,
    epochs=300,
    verbose=True
)

# The CopulaGAN model trains on the original dataset to learn pattern and relationships (ex: what the synthetic dataset should contain)
synthesizer.fit(real_data)

# A 1,000 row synthetic dataset is generated from the CopulaGAN model
synthetic_data = synthesizer.sample(num_rows=1000)
        """, language="python")



# Synthesizer Comparison Table
st.markdown("""
---

The Synthetic Data Vault (SDV) offers a range of synthesizers. Each mdoel is designed with own strengths, limitations, and ideal use cases.

### A Quick Guide to Different SDV Synthesizers:

| Model              | Type of Data           | Strengths                                           | Limitations                    | Speed                   |
|--------------------|------------------------|-----------------------------------------------------|--------------------------------|-------------------------|
| **CTGAN**          | Numerical, Categorical | High quality on complex, imbalanced data            | Requires tuning                | ⏳ Slow                 |
| **TVAE**           | Numerical, Categorical | Captures non-linear patterns well                   | Higher resource demand          | ⚖️ Medium              |
| **GaussianCopula** | Mostly Numerical       | Fast, easy to use                                   | Struggles with complex/mixed data | ⚡ Fast             |
| **CopulaGAN**      | Numerical, Categorical | Combines GANs with statistical copulas for balance  | Newer model, fewer benchmarks   | ⚡ Fast                 |

""")


# Final Navigation Tip
st.markdown("""
---

### Next Up: The Process 🧭 

You’ve now met the four core models. Let’s move on to the next chapter, where you’ll walk through the full **process* for generating and evaluating synthetic data step-by-step.
""")
