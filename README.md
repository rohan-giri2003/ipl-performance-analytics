cat << 'EOF' > README.md
# 🏏 IPL Performance & Strategy Intelligence Platform (2008–2020)

An end-to-end cricket analytics platform examining match outcomes, franchise consistency, venue-specific trends, and ball-by-ball player metrics across 1,000+ Indian Premier League fixtures.

🔗 **Live Interactive App:** [View IPL Dashboard](https://ipl-performance-analytics.streamlit.app/)

---

## 📌 Analytical Findings & Strategic Takeaways
* **Franchise Dominance:** Mumbai Indians (144 wins) and Chennai Super Kings lead historical win rates across tournament editions.
* **Toss Impact & Chasing Advantage:** Over 61% of toss winners opt to field first, with night fixtures exhibiting a measurable chasing advantage due to dew factors and pitch stabilization.
* **Milestone Analytics:** Isolates all-time batting runs (Orange Cap contenders) and bowling dismissals (Purple Cap leaders, filtering out non-bowler dismissals like run outs).

---

## 🛠️ Tech Stack
* **Language & Analysis:** Python, Pandas, NumPy
* **Visualizations:** Plotly Express
* **Application Framework:** Streamlit Community Cloud
* **Version Control:** Git, GitHub

---

## ⚙️ Data Pipeline & Architecture
1. **Entity Harmonization:** Unified franchise identity transitions across seasons (e.g., Delhi Daredevils to Delhi Capitals, Rising Pune Supergiants variants).
2. **Feature Optimization:** Curated deliveries data down to essential scoring and dismissal attributes (`matches_cleaned.csv`, `deliveries_cleaned.csv`) for minimal latency.
3. **Reactive UI:** Leveraged `@st.cache_data` for near-instant client-side filtering across teams and metric slices.

---

## 🚀 Local Run
```bash
git clone [https://github.com/rohan-giri2003/ipl-performance-analytics.git](https://github.com/rohan-giri2003/ipl-performance-analytics.git)
cd ipl-performance-analytics
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
