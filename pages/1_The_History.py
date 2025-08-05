import streamlit as st

st.set_page_config(page_title="Chapter 1: The History 🏛️", layout="wide")

# Page title
st.title("Chapter 1: The History 🏛️")

# Introduction
st.markdown("""

Welcome to the history of synthetic data!

In this chapter, you’ll learn how synthetic data began as a solution to privacy concerns in public datasets **and** how it evolved into a key tool for secure, scalable, and ethical data science.

---

### 📉 What’s the Hidden Challenge Behind AI’s Growth?

Artificial intelligence holds the key to solving the world’s most complex problems. However, it's growth is dependant on the quality and availability of training data. 

Currently, there are two major roadblocks: 

- **Data Scarcity**  
  The shortage of high-quality labeled data

- **Data Security**  
  The lack of access to proprietary data

These challenges are acute for regulated industries like healthcare and finance where access to sensitive data is highly controlled.  

Organizations of all sizes, from small teams to Fortune 500 companies, have started to ask, “Where do we find or create the data we need to make my AI application work?” 

---

### 💡 Is There A Better Way To Get Training Data? 

To address these challenges, researchers and organizations have explored different strategies:

- Collaborating – Partnering with data owners to access secure datasets  
- Cleaning – Preparing datasets to be usable for AI and modeling  
- Simplifying – Using simpler models to create smaller, safe datasets  
- **Generating – Creating new datasets that mimic the original, but pose no privacy risk**

Generating has stood out as the most scalable and privacy-safe solution. 

Today, over 60% of AI training data is synthetic. 

By 2030, Synthetic Data is expected to overshadow real data when training AI models and will generate over $2.3 billion in market value! 

---
### 🧠 What is Synthetic Data?

**Synthetic data** refers to artificially generated datasets that replicate the structure and statistical behavior of real-world data without exposing any private information!

This allows data scientists to train and test AI tools with data that is safe to share. 
 
---
### 📜 Who First Invented Synthetic Data and Why? 

The synthetic data may seem like a cutting-edge innovation, but its origins stretch back more than 30 years.

In 1993, the U.S. Census Bureau faced a dilemma: How could the agency share detailed individual survey responses for research **without revealing private identities**? 

Statistician **Donald Rubin** proposed using statistical models to generate synthetic records that mimicked the real dataset, but did not contain any actual records. 
This breakthrough proved it was possible to protect privacy while ensuring public access to data. 

Since then, synthetic data generation techniques have evolved dramatically. Users can “digitally generate the data that they need, on demand, in whatever volume they require, tailored to their precise specifications". 

Modern synthetic generative platforms, like MostlyAI, Gretel, and YData, have been used to:   
- Diagnose medical conditions using synthetic patient records 
- Test financial systems under stress without real transactions 
- Train autonomous vehicles using simulated crash data

---
### 🔍 Can Synthetic Data Be Trusted?

As synthetic data usage becomes more common, a new challenge arises: How can we know if the Synthetic Data is “Good”?

There are three pillars of synthteic data evaluation:

1. **Accuracy** – How well does the synthetic data reflect the patterns and relationships in the original?
2. **Utility** – Can machine learning models trained on the synthetic data produce accurate results?
3. **Privacy** – How unlikely is it that anyone could re-identify individuals from the synthetic dataset?

This course will walk you through the full process of generating and evaluating synthetic datasets that meet these critical standards. 


---

### Next Up: The Models ⚙️

Now that you understand the motive behind synthetic data creation, let’s explore the **four foundational models** that generate it.

---
**References**
- Sciforce. (2024, December 10). Synthetic data: A passing trend or the future of ai?. Medium. https://medium.com/sciforce/synthetic-data-a-passing-trend-or-the-future-of-ai-65a64e3234b7 
- Toews, R. (2023, October 5). Synthetic data is about to transform artificial intelligence. Forbes. https://www.forbes.com/sites/robtoews/2022/06/12/synthetic-data-is-about-to-transform-artificial-intelligence/ 
- Villalobos, P., Ho, A., Sevilla, J., Besiroglu, T., Heim, L., & Hobbhahn, M. (2024, June 6). Will we run out of data? limits of LLM scaling based on human-generated data. Epoch AI. https://epoch.ai/blog/will-we-run-out-of-data-limits-of-llm-scaling-based-on-human-generated-data 
- Watson, A. (2025, January 10). 2025: The year synthetic data goes mainstream. RSS. https://gretel.ai/blog/2025-the-year-synthetic-data-goes-mainstream#:~:text=Synthetic%20data%20can%3A,market%20trends%2C%20or%20compliance%20rules.  

""")


