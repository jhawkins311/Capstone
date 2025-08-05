import streamlit as st

st.set_page_config(page_title="Chapter 3: The Process", layout="wide")
st.title("Chapter 3: The Process 🧭")

st.markdown("""
Welcome! This is your **step-by-step guide** to generating and evaluating synthetic data—**no coding required**.

If you want to use our Lab but don’t want to touch code, you’re in the right place.
Each tab below walks you through a key stage, with clear instructions and images for every step.
""")

tab1, tab2, tab3, tab4 = st.tabs([
    "📂 Preparing",
    "🧠 Training",
    "⚙️ Generating",
    "📊 Evaluating"
])

with tab1:
    st.header("📂 Preparing")
    st.markdown("""
Start by getting your environment and data ready. This section covers **steps 1–4**.

---

**Step 1: Install Required Tools**

To run the Lab, make sure the right tools are installed.  
These include SDV, Pandas, Plotly, and other helpers.

*Why this matters:*  
Without these, nothing else can work!

""")
    st.image("path_to_image1.png", caption="Installing required tools")

    st.markdown("""
**Step 2: Import Libraries**

The Lab loads all the needed features in the background.

*Why this matters:*  
All buttons and options you see rely on these libraries.

""")
    st.image("path_to_image2.png", caption="Libraries loaded")

    st.markdown("""
**Step 3: Upload Your Data**

You’ll upload your spreadsheet (CSV or Excel file) in the Lab interface.

- Your data should have just **one table** (no extra sheets).
- The Lab will show you how many rows and columns it found.

*Why this matters:*  
This is the real data that the tool will learn from.

""")
    st.image("path_to_image3.png", caption="Upload your data file")

    st.markdown("""
**Step 4: Manage Sensitive Columns**

You’ll get a chance to **remove** or **scramble** private columns (like Name or ZIP code) before the tool learns from your data.

- Remove: The column is deleted from the process
- Scramble: The column is mixed up, breaking any links to individuals

*Why this matters:*  
Taking out sensitive info protects privacy—even before creating synthetic data.

""")
    st.image("path_to_image4.png", caption="Remove or scramble sensitive columns")

    st.info("**Tip:** Only upload data you have permission to use. Remove or scramble anything private before moving on!")


with tab2:
    st.header("🧠 Training")
    st.markdown("""
Now the Lab will study your data using four different approaches. This covers **steps 5–6**.

---

**Step 5: Create Metadata**

The tool will **automatically figure out** what types of information are in your table—numbers, categories, dates, etc.  
You’ll see a visual summary before moving ahead.

*Why this matters:*  
The more accurate this summary, the more realistic your synthetic data will be.

""")
    st.image("path_to_image5.png", caption="Metadata summary preview")

    st.markdown("""
**Step 6: Train Multiple Models**

The Lab uses **four different engines** (CTGAN, TVAE, GaussianCopula, CopulaGAN) to learn from your data.
- Each engine tries a different method—so you get more than one result to compare.

*Why this matters:*  
No single engine works best for all data! More models = more choices for your project.

""")
    st.image("path_to_image6.png", caption="Training progress for multiple models")

    st.warning("Training will run quickly for a demo (10 rounds), but for final results, ask for a longer training time.")



with tab3:
    st.header("⚙️ Generating")
    st.markdown("""
Time to create your synthetic datasets! This section covers **steps 7–8**.

---

**Step 7: Generate Synthetic Data**

The Lab will ask how many rows you want.  
Each engine creates its own synthetic table—mimicking your original data, but without direct copies.

*Why this matters:*  
This gives you a brand-new dataset for analysis, sharing, or AI training—without exposing the real data.

""")
    st.image("path_to_image7.png", caption="Choose number of synthetic rows")

    st.markdown("""
**Step 8: Download Your Datasets**

You’ll get a **single Excel file** with a tab for each synthetic model.

*Why this matters:*  
You can open, share, or further analyze these new datasets—each from a different model.

""")
    st.image("path_to_image8.png", caption="Download your synthetic datasets")

    st.success("Each synthetic table is labeled by the model that created it. Compare them to find the best fit!")



with tab4:
    st.header("📊 Evaluating")
    st.markdown("""
Now let’s see how good your synthetic datasets are! This covers **steps 9–10**.

---

**Step 9: Evaluate All Synthetic Datasets**

The Lab checks three big things for each synthetic dataset:
- **Accuracy:** Does the shape match the real data?
- **Quality:** Are the patterns similar?
- **Privacy:** Does it protect from revealing real individuals?

*Why this matters:*  
Not all synthetic data is created equal. You need to know which version is safest and most realistic.

""")
    st.image("path_to_image9.png", caption="See evaluation results for all models")

    st.markdown("""
**Step 10: Get Recommendations and a Report**

You’ll see a **dashboard** that highlights the best synthetic dataset, and you can download a detailed Word report for your records.

*Why this matters:*  
This makes it easy to choose the best synthetic data for your needs—and have proof for compliance or team review.

""")
    st.image("path_to_image10.png", caption="Dashboard and report preview")

    st.success("You’ve completed all ten steps! Your synthetic data is now ready to use or share—privacy evaluated and results documented.")


# Final Navigation Tip
st.markdown("""
---

### Next Up: The Lab 🧪

Now that you have seen how analysts generate and evaluate synthetic data, now you can try!
""")
