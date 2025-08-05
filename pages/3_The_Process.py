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
    st.header("📁 Section 1: Preparing")

    # Step 1
    st.subheader("1. Install Dependencies")
    st.markdown("""
To run the Lab, you’ll need to install the required tools (like SDV, Pandas, Plotly, and others).
These handle all data processing and synthetic generation.

*Why this matters:*  
Without these, nothing else works!
""")
    st.image("path_to_image1.png", caption="Installing required tools")

    # Step 2
    st.subheader("2. Import Libraries")
    st.markdown("""
Once installed, the Lab loads all the features it needs behind the scenes.
You don’t need to do anything! just watch for a “Success” message.

*Why this matters:*  
All buttons and features in the notebook rely on these libraries.
""")
    st.image("path_to_image2.png", caption="Libraries loaded and ready")

    # Step 3
    st.subheader("3. Upload File")
    st.markdown("""
Upload your dataset in `.csv` or `.xlsx` format using the Lab’s interface.
- Your data should have just **one table**.
- The Lab will tell you how many rows and columns it found.

*Why this matters:*  
This is the real data that the Lab will use to learn patterns and relationships.
""")
    st.image("path_to_image3.png", caption="Upload your data file")

    # Optional: Manage Sensitive Columns
    st.subheader("Optional: Manage Sensitive Columns")
    st.markdown("""
Before moving on, you’ll have the chance to **remove** or **scramble** private columns (like Name, Email, or ZIP code).
- **Remove:** Deletes the column before modeling.
- **Scramble:** Mixes up column values to break connections.

*Why this matters:*  
Taking out sensitive info protects privacy—even before creating synthetic data.
""")
    st.image("path_to_image4.png", caption="Remove or scramble sensitive columns")

    # Step 4
    st.subheader("4. Create Metadata")
    st.markdown("""
The Lab automatically detects what type of information is in your data: numbers, categories, dates, etc.
You’ll see a visual summary to check for accuracy before moving ahead.

*Why this matters:*  
Accurate metadata means more realistic and reliable synthetic data.
""")
    st.image("path_to_image5.png", caption="Metadata summary preview")

    st.info("**Tip:** Only upload data you have permission to use. Remove or scramble anything private before moving on!")


with tab2:
    st.header("🧠 Section 2: Training")

    # Step 5
    st.subheader("5. Train Synthesizers (10 Epochs)")
    st.markdown("""
The Lab uses **four different engines**, CTGAN, TVAE, GaussianCopula, and CopulaGAN, to learn from your data.
Each engine tries a different method, so you get a bunch of results to compare.

- Training is set for 10 rounds (epochs) by default for speed.
- For best results, use more epochs when time allows!

*Why this matters:*  
No single engine works best for all data. Training multiple models gives you options for the best synthetic output.
""")
    st.image("path_to_image6.png", caption="Training progress for multiple models")

    st.warning("Training runs quickly for demos (10 epochs), but for final results, ask for a longer training time.")


with tab3:
    st.header("⚙️ Section 3: Generating")

    # Step 6
    st.subheader("6. Generate Synthetic Datasets")
    st.markdown("""
Choose how many rows of synthetic data you want.  
Each engine creates its own synthetic table. This mimics your original data, but doesn't copy it.

*Why this matters:*  
This gives you new, privacy-safe datasets for analysis, sharing, or AI training.
""")
    st.image("path_to_image7.png", caption="Choose number of synthetic rows")

    # Step 7
    st.subheader("7. Download Synthetic Datasets (Excel File)")
    st.markdown("""
Download a single Excel file containing a tab for each synthetic dataset (one per model).

*Why this matters:*  
You can open, share, or analyze these new datasets—each created by a different model.
""")
    st.image("path_to_image8.png", caption="Download your synthetic datasets")

    st.success("Each synthetic table is labeled by the model that created it. Compare them to find the best fit!")


with tab4:
    st.header("📊 Section 4: Evaluating")

    # Step 8
    st.subheader("8. Generate Evaluation Scores")
    st.markdown("""
The Lab checks each synthetic dataset for:
- **Accuracy (Diagnostic):** Does it match the structure of your real data?
- **Quality (Utility):** Are the statistical patterns and relationships similar?
- **Privacy Risk:** Does it protect real individuals from being identified?

*Why this matters:*  
Not all synthetic data is created equal! These tests show which version is safest and most realistic.
""")
    st.image("path_to_image9.png", caption="Evaluation results for all models")

    # Step 9a: Dashboard Visualizations and Explanations
    st.subheader("9a. Generating Evaluation Dashboard")
    st.markdown("""
After scoring, you’ll see a **dashboard** with several charts.  
Here’s what each one means and why it’s important:
""")

    # 1️⃣ Accuracy Chart
    st.markdown("**1️⃣ Accuracy (Diagnostic Score) Bar Chart**")
    st.image("path_to_accuracy_chart.png", caption="Accuracy comparison across models")
    st.info("""
Shows how well each synthetic dataset preserves the structure and rules of your real data (like value ranges, missing values, unique IDs).  
**Why it matters:**  
High accuracy means the synthetic data is structurally faithful, so any analysis or database loading works smoothly.  
Low accuracy? That model might be missing important patterns.
""")

    # 2️⃣ Utility Chart
    st.markdown("**2️⃣ Utility (Quality Score) Bar Chart**")
    st.image("path_to_quality_chart.png", caption="Utility comparison across models")
    st.info("""
Shows how well the synthetic data mimics the statistical distributions and relationships of the original data.  
**Why it matters:**  
High utility means your synthetic data is *useful*. This means analytics and AI models will behave as expected.  
Low utility? The data may “look right” but can lead to misleading insights.
""")

    # 3️⃣ Privacy Chart
    st.markdown("**3️⃣ Privacy (DCR Score) Bar Chart**")
    st.image("path_to_privacy_chart.png", caption="Privacy risk scores for each model")
    st.info("""
Shows the privacy risk for each synthetic dataset (lower is better).  
**Why it matters:**  
A low privacy risk score means the synthetic data offers strong protection against re-identification; this is crucial for privacy compliance and ethical use.
""")

    # 4️⃣ Column Comparison Plot
    st.markdown("**4️⃣ Column Comparison Plot**")
    st.image("path_to_column_comparison.png", caption="Distribution comparison for a selected column")
    st.info("""
Lets you pick a column and compare its values in the real vs. synthetic datasets.  
**Why it matters:**  
Helps you see if each model captures detailed patterns for individual features: great for spotting overfitting, underfitting, or outliers.
""")

    # 5️⃣ Per-Column Similarity Chart
    st.markdown("**5️⃣ Per-Column Similarity Bar Chart**")
    st.image("path_to_column_similarity.png", caption="Per-column quality scores for a selected model")
    st.info("""
Shows how well each individual column was reproduced in a selected synthetic dataset.  
**Why it matters:**  
Helps diagnose which features were well-learned and which need improvement. This “heat map” helps with model selection and tuning.
""")

    # 6️⃣ Composite Recommendation
    st.markdown("**6️⃣ Composite Recommendation & Overall Score**")
    st.image("path_to_composite_score.png", caption="Best overall model highlighted")
    st.info("""
Summarizes the scores and recommends the best synthetic dataset overall, balancing accuracy, utility, and privacy.  
**Why it matters:**  
Gives you a clear, one-glance answer: Which synthetic data is safest and most useful for your needs.
""")

    st.success("This dashboard makes it easy to understand and justify your synthetic data choices... even if you’re not a data scientist!")

    # Step 9b: Report
    st.subheader("9b. Generate Evaluation Report (Word Document)")
    st.markdown("""
Download a Word report for documentation, compliance, or sharing with your team.
- The report summarizes all your results and recommendations.

*Why this matters:*  
You have a record of your process, comparisons, and proof of privacy protection.
""")
    st.image("path_to_image11.png", caption="Download the evaluation report")


# Final Navigation Tip
st.markdown("""
---

### Next Up: The Lab 🧪

Now that you have seen how analysts generate and evaluate synthetic data, now you can try!
""")
