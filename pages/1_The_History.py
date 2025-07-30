import streamlit as st

# Page title
st.title("Chapter 1: The History")

# Introduction
st.markdown("""

Welcome to Chapter 1: Origins of the Synthetic Data 101 course!

In this chapter, you’ll explore the history and motivation behind synthetic data. You’ll learn how it began as a solution to privacy concerns in public datasets—and how it evolved into a key tool for secure, scalable, and ethical data science.

---

### 📜 The Origin
Synthetic data may seem like a cutting-edge innovation, but its origins stretch back over 30 years.

In 1993, the U.S. Census Bureau faced a dilemma: how could it share detailed individual survey responses for research and policy purposes **without revealing private identities**? 

The answer came from statistician Donald Rubin, who proposed using **statistical models** to generate synthetic data that mirrored the real dataset—without including any actual records. 
His approach protected privacy while enabling public access. 

This laid the foundation for today’s synthetic data movement.

---

### 📉 The Two Major Roadblocks

As the demand for data grew, two major challenges began to limit access to useful datasets:

- **Data Scarcity**  
  The shortage of high-quality, labeled, or representative datasets.

- **Data Security**  
  The legal, ethical, and technical risks of sharing sensitive public or private data.

These roadblocks persist today—especially in regulated industries like **healthcare, finance, and education**.

---

### 🔧 Possible Solutions

To overcome these challenges, researchers and organizations adopted a new set of strategies:

- **Collaborating** – Partnering with data owners to access secure datasets  
- **Cleaning** – Preparing datasets to be usable for AI and modeling  
- **Simplifying** – Using simpler models to create smaller, safe datasets  
- **Generating** – Creating new datasets that mimic the original, but pose no privacy risk

---

### 🧠 Enter: Synthetic Data

> Synthetic data refers to **artificially generated datasets** that mimic real-world data in **structure and behavior**—while **avoiding any privacy risks**.

Modern tools like **MostlyAI**, **Gretel**, and **YData** generate synthetic records that can be used to:
- Diagnose medical conditions faster  
- Test financial systems under stress  
- Train autonomous vehicles without physical crashes

---

### 📏 How Do We Evaluate Synthetic Data?

Synthetic datasets are evaluated based on three core criteria:

1. **Accuracy** – How well does the synthetic data reflect the patterns and relationships in the original?
2. **Utility** – Can machine learning models trained on the synthetic data produce accurate results?
3. **Privacy** – How unlikely is it that anyone could re-identify individuals from the synthetic dataset?

A 2025 study by JP Morgan showed that high-quality synthetic data could power fraud detection models—**without violating privacy regulations**.

---

### 🧪 Next Up: The Models

Now that you understand the origin story and purpose of synthetic data, let’s explore the **four foundational models** that generate it.
""")
