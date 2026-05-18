# 🏥 Diabetic Readmission Prediction

An interactive Streamlit web application that demonstrates a complete Pattern Recognition pipeline for predicting hospital readmission of diabetic patients.

**Pattern Recognition · DA360 · Yarmouk University**

---

## 📖 About the Project

This project applies machine learning and pattern recognition techniques to the **Diabetes 130-US Hospitals (1999–2008)** dataset from the UCI Machine Learning Repository. The goal is to predict whether a diabetic patient will be readmitted to the hospital, and if so, within what timeframe.

The application showcases the full ML workflow — from data exploration to live prediction — through an interactive web interface, complemented by a Power BI dashboard for business-intelligence-style insights.

---

## ✨ Features

- 📊 **Data Exploration** — Interactive charts, missing value analysis, demographics
- 🔧 **Preprocessing Pipeline** — Step-by-step visualization of data cleaning
- 🎯 **Feature Selection** — Random Forest importance, correlation heatmap, PCA
- 🤖 **Model Comparison** — Decision Tree, k-NN, SVM, and Logistic Regression
- 🔮 **Live Prediction** — Real-time risk scoring for new patient profiles
- 📈 **Power BI Dashboard** — Embedded business intelligence view
- 📝 **Conclusions** — Findings, limitations, and future work

---

## 🚀 Running Locally

### Prerequisites
- Python 3.9 or higher
- pip

### Installation

```bash
pip install -r requirements.txt
streamlit run Home.py
```

> The dataset will be **automatically downloaded** from the UCI repository on first launch.

The app will open in your browser at `http://localhost:8501`.

---

## 🌐 Deploying to GitHub

### 1. Create a GitHub Account
Sign up at [github.com](https://github.com) if you don't already have an account.

### 2. Create a New Repository
- Click **"+" → New repository**
- Name: `diabetic-readmission-prediction`
- Choose **Public**
- ✅ Add a README file
- Click **Create repository**

### 3. Upload the Project Files
- In the repository page, click **"Add file" → "Upload files"**
- Drag and drop **the contents** of the `streamlit_app` folder, **except**:
  - ❌ `diabetic_data.csv` (will be auto-downloaded)
  - ❌ `__pycache__/` folders
  - ❌ `power_BI_460.pbix` (large file, upload separately if needed)
- Click **Commit changes**

---

## ☁️ Deploying to Streamlit Cloud (Free)

### 1. Go to [share.streamlit.io](https://share.streamlit.io)

### 2. Sign in with GitHub

### 3. Click **"New app"**

### 4. Fill in the deployment settings:
- **Repository:** `your-username/diabetic-readmission-prediction`
- **Branch:** `main`
- **Main file path:** `Home.py`

### 5. Click **Deploy!**

Within 2-3 minutes, you'll get a public URL like:
```
https://your-app-name.streamlit.app
```

Share it with anyone — no installation required! 🎉

---

## 📊 Adding the Power BI Dashboard

The app includes a dedicated **Dashboard** page that can embed your Power BI report.

### Option 1: Live Embed (Recommended)

1. Sign up for a free account at [powerbi.microsoft.com](https://powerbi.microsoft.com)
2. Open `power_BI_460.pbix` in Power BI Desktop
3. Click **Publish** → choose **My workspace**
4. In Power BI Service: open the report → **File → Embed report → Publish to web (public)**
5. Copy the URL from the iframe `src` attribute
6. Open `pages/7_Dashboard.py` and replace:

```python
POWER_BI_EMBED_URL = "https://app.powerbi.com/view?r=YOUR_REPORT_ID_HERE"
```

with your actual embed URL.

### Option 2: Static Screenshots

1. Take screenshots of your Power BI dashboard from Power BI Desktop
2. Place them in `assets/dashboard_screenshots/`
3. The page will display them automatically

---

## 📁 Project Structure

```
streamlit_app/
│
├── Home.py                       ← Landing page
├── requirements.txt              ← Python dependencies
├── README.md                     ← This file
├── .gitignore                    ← Git ignore rules
│
├── .streamlit/
│   └── config.toml               ← Theme configuration
│
├── assets/                       ← Static assets (optional)
│
└── pages/
    ├── 1_Data_Exploration.py
    ├── 2_Preprocessing.py
    ├── 3_Feature_Selection.py
    ├── 4_Models_Results.py
    ├── 5_Live_Prediction.py
    ├── 6_Conclusion.py
    └── 7_Dashboard.py            ← Power BI integration
```

---

## 🎨 Design System

### Color Palette

| Color | Hex Code | Usage |
|-------|----------|-------|
| Teal Dark | `#2A6F6F` | Headers, primary actions |
| Teal Medium | `#4A9B9B` | Secondary elements |
| Teal Light | `#8AC4C4` | Accents, highlights |
| Coral | `#D97757` | Warnings, secondary data |
| Gray | `#A8A8A8` | Neutral elements |
| Background | `#F5F5F0` | Page background |
| Text Dark | `#2C3E3E` | Primary text |

---

## 🛠️ Technologies Used

- **Streamlit** — Web framework
- **Plotly** — Interactive visualizations
- **Pandas / NumPy** — Data manipulation
- **scikit-learn** — Machine learning models
- **imbalanced-learn (SMOTE)** — Class balance handling
- **Power BI** — Business intelligence dashboard

---

## ⚙️ Customization Before Submission

### In `pages/4_Models_Results.py`:
Update the `results` dictionary and `cms` confusion matrices with your actual model outputs from the training notebook.

### In `Home.py`:
Replace the placeholder team member names with your actual team.

### In `pages/7_Dashboard.py`:
Add your Power BI embed URL (see "Adding the Power BI Dashboard" section above).

---

## 📚 Dataset

- **Name:** Diabetes 130-US Hospitals for Years 1999–2008
- **Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Diabetes+130-US+hospitals+for+years+1999-2008)
- **Size:** ~101,766 records, 50 features
- **Task:** Multiclass classification (3 classes: NO / <30 days / >30 days)

---

## 👥 Team

Replace this section with your team members' names.

- Member 1
- Member 2
- Member 3

---

## 📄 License

This project is created for academic purposes as part of the Pattern Recognition (DA360) course at Yarmouk University.

---

**Pattern Recognition Project · DA360 · Yarmouk University · 2026**
