import streamlit as st

# Page Layout & Title
st.set_page_config(page_title="Chapter 2: Models", layout="wide")
st.title("Chapter 2: Models")

# Page Description
st.markdown("""
Welcome to **Chapter 2: Models** of the Synthetic Data 101 course!

In this chapter, you'll explore four foundational models from the [Synthetic Data Vault (SDV)](https://docs.sdv.dev/) library. 

These models, referred to as **Synthesizers**, specialize in generating synthetic versions of single-table datasets by learning the structure and relationships within the real data.

Each model has its own strengths, limitations, and ideal use cases. Think of them as different tools in your synthetic data toolbox!
""")

# Synthesizer Comparison Table
st.markdown("""
---

### 🧰 Comparison Table: SDV Synthesizers

| Model              | Type of Data           | Strengths                                           | Limitations                    | Speed                   |
|--------------------|------------------------|-----------------------------------------------------|--------------------------------|-------------------------|
| **CTGAN**          | Numerical, Categorical | High quality on complex, imbalanced data            | Requires tuning                | ⏳ Slow                 |
| **TVAE**           | Numerical, Categorical | Captures non-linear patterns well                   | Higher resource demand          | ⚖️ Medium              |
| **GaussianCopula** | Mostly Numerical       | Fast, easy to use                                   | Struggles with complex/mixed data | ⚡ Fast             |
| **CopulaGAN**      | Numerical, Categorical | Combines GANs with statistical copulas for balance  | Newer model, fewer benchmarks   | ⚡ Fast                 |
""")

# --- CTGAN Section ---
st.markdown("""
---

### 🧪 CTGAN — Conditional GAN for Tabular Data
The **CTGAN Synthesizer** uses a GAN-based approach where a generator and discriminator compete to improve output quality. It’s particularly effective on **imbalanced** and **mixed-type** datasets (e.g., medical or credit data). CTGAN can take longer to train but often produces high-fidelity results that preserve deep feature relationships.

> Best for: High-stakes, highly structured datasets where accuracy matters most.
""")

with st.expander("🧠 Show CTGAN Example Code"):
    st.code("""
from sdv.single_table import CTGANSynthesizer

synthesizer = CTGANSynthesizer(
    metadata,           # required
    enforce_rounding=False,
    epochs=500,
    verbose=True
)
synthesizer.fit(real_data)
synthetic_data = synthesizer.sample(num_rows=1000)
    """, language="python")

# --- TVAE Section ---
st.markdown("""

### 🔄 TVAE — Tabular Variational Autoencoder
The **TVAE Synthesizer** relies on **variational autoencoders** (VAEs), which compress and reconstruct the dataset to learn its structure. This makes it great for capturing **non-linear patterns** in data—like complex interactions between features.

> Best for: Mid-size datasets where relationships between variables are important.
""")

with st.expander("🧠 Show TVAE Example Code"):
    st.code("""
from sdv.single_table import TVAESynthesizer

synthesizer = TVAESynthesizer(
    metadata,           # required
    enforce_rounding=False,
    epochs=300,
    verbose=True
)
synthesizer.fit(real_data)
synthetic_data = synthesizer.sample(num_rows=1000)
    """, language="python")

# --- GaussianCopula Section ---
st.markdown("""

### 📈 GaussianCopula — Classic but Powerful
The **GaussianCopula Synthesizer** is the simplest of the four. It uses classic statistical transformations to model relationships, assuming a multivariate normal structure. While limited to mostly numerical data, it’s **very fast** and **easy to use**, making it ideal for prototyping or educational use.

> Best for: Quick generation of synthetic data when speed or simplicity is a priority.
""")

with st.expander("🧠 Show GaussianCopula Example Code"):
    st.code("""
from sdv.single_table import GaussianCopulaSynthesizer

synthesizer = GaussianCopulaSynthesizer(metadata)
synthesizer.fit(real_data)
synthetic_data = synthesizer.sample(num_rows=1000)
    """, language="python")

# --- CopulaGAN Section ---
st.markdown("""

### 🧬 CopulaGAN — Hybrid Approach
The **CopulaGAN Synthesizer** is a **hybrid model** that blends GANs with statistical copulas. It offers a middle ground between deep learning complexity and traditional modeling, aiming to balance **accuracy**, **privacy**, and **speed**.

> Best for: Scenarios that demand both performance and speed, such as limited-resource environments or pilot testing.
""")

with st.expander("🧠 Show CopulaGAN Example Code"):
    st.code("""
from sdv.single_table import CopulaGANSynthesizer

synthesizer = CopulaGANSynthesizer(
    metadata,
    enforce_rounding=False,
    epochs=300,
    verbose=True
)
synthesizer.fit(real_data)
synthetic_data = synthesizer.sample(num_rows=1000)
    """, language="python")

# Final Navigation Tip
st.markdown("""
---

### 🧭 Next Up: Workflow

You’ve now met the four core models. Let’s move on to the next chapter, where you’ll walk through the full **workflow** for generating and evaluating synthetic data step-by-step.
""")
