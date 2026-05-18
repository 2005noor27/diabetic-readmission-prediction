"""
Page: Preprocessing
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Preprocessing", page_icon="🔧", layout="wide")

TEAL_DARK = "#2A6F6F"
TEAL_MEDIUM = "#4A9B9B"
TEAL_LIGHT = "#8AC4C4"
CORAL = "#D97757"
GRAY = "#A8A8A8"

st.markdown("""
<style>
    .page-header {
        background: linear-gradient(135deg, #2A6F6F 0%, #4A9B9B 100%);
        padding: 2rem; border-radius: 12px;
        color: white; margin-bottom: 2rem;
    }
    .page-header h1 { color: white !important; margin: 0; }
    .page-header p { color: rgba(255,255,255,0.95); margin: 0.5rem 0 0 0; }
    
    .step-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #2A6F6F;
        margin-bottom: 1rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    
    .step-number {
        display: inline-block;
        background: #2A6F6F;
        color: white;
        width: 32px; height: 32px;
        border-radius: 50%;
        text-align: center;
        line-height: 32px;
        font-weight: 600;
        margin-right: 0.5rem;
    }
    
    .step-title {
        color: #2A6F6F;
        font-weight: 600;
        font-size: 1.1rem;
        display: inline;
    }
    
    .section-header {
        color: #2A6F6F;
        font-weight: 600;
        margin-top: 2rem;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #8AC4C4;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="page-header">
    <h1>🔧 Data Preprocessing</h1>
    <p>Transforming raw data into a clean, ML-ready format</p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# PREPROCESSING PIPELINE
# ============================================================
st.markdown('<h3 class="section-header">Preprocessing Pipeline</h3>', unsafe_allow_html=True)

steps = [
    {
        "num": 1,
        "title": "Replace Placeholders",
        "desc": "Replaced '?' values with NaN to enable proper missing-value handling using pandas and numpy.",
        "code": "df.replace('?', np.nan, inplace=True)"
    },
    {
        "num": 2,
        "title": "Drop High-Missing Columns",
        "desc": "Removed columns with excessive missing rates: weight (~97%), payer_code (~40%), medical_specialty (~49%), max_glu_serum, A1Cresult.",
        "code": "df.drop(columns=['weight','payer_code','medical_specialty','max_glu_serum','A1Cresult'], inplace=True)"
    },
    {
        "num": 3,
        "title": "Drop IDs & Duplicates",
        "desc": "Removed encounter_id and patient_nbr (non-informative identifiers) and eliminated duplicate rows.",
        "code": "df.drop(columns=['encounter_id','patient_nbr'], inplace=True)\ndf.drop_duplicates(inplace=True)"
    },
    {
        "num": 4,
        "title": "Impute Missing Values",
        "desc": "Categorical columns filled with mode (most frequent value); numerical columns filled with median (robust to outliers).",
        "code": "df[col].fillna(df[col].mode()[0], inplace=True)  # categorical\ndf[col].fillna(df[col].median(), inplace=True)    # numerical"
    },
    {
        "num": 5,
        "title": "Label Encoding",
        "desc": "Converted categorical features and the target variable into numerical labels using sklearn's LabelEncoder.",
        "code": "le = LabelEncoder()\ndf[col] = le.fit_transform(df[col].astype(str))"
    },
    {
        "num": 6,
        "title": "Train/Test Split",
        "desc": "Stratified 80/20 split to preserve class distribution across training and testing sets.",
        "code": "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)"
    },
    {
        "num": 7,
        "title": "Standardization",
        "desc": "Applied StandardScaler so all features have mean=0 and std=1, ensuring fair weighting in distance-based algorithms.",
        "code": "scaler = StandardScaler()\nX_train_scaled = scaler.fit_transform(X_train)\nX_test_scaled = scaler.transform(X_test)"
    },
    {
        "num": 8,
        "title": "SMOTE Oversampling",
        "desc": "Applied Synthetic Minority Oversampling Technique to balance the three classes in training data.",
        "code": "smote = SMOTE(random_state=42)\nX_train_bal, y_train_bal = smote.fit_resample(X_train_scaled, y_train)"
    },
]

for step in steps:
    with st.expander(f"Step {step['num']}: {step['title']}", expanded=False):
        st.markdown(f"<p style='color:#2C3E3E; line-height:1.7;'>{step['desc']}</p>", unsafe_allow_html=True)
        st.code(step['code'], language='python')

# ============================================================
# SMOTE VISUALIZATION
# ============================================================
st.markdown('<h3 class="section-header">Class Balance: Before vs. After SMOTE</h3>', unsafe_allow_html=True)

# Simulated illustration (placeholder values typical for this dataset)
before_smote = {'NO': 43900, '>30': 28400, '<30': 8800}
after_smote = {'NO': 43900, '>30': 43900, '<30': 43900}

col1, col2 = st.columns(2)

with col1:
    fig = go.Figure(data=[go.Bar(
        x=list(before_smote.keys()),
        y=list(before_smote.values()),
        marker_color=[TEAL_DARK, TEAL_LIGHT, CORAL],
        text=list(before_smote.values()),
        textposition='outside'
    )])
    fig.update_layout(
        title="Before SMOTE — Imbalanced",
        plot_bgcolor='white', paper_bgcolor='white',
        height=400, font=dict(color="#2C3E3E"),
        yaxis=dict(title='Sample Count'),
        xaxis=dict(title='Class')
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig = go.Figure(data=[go.Bar(
        x=list(after_smote.keys()),
        y=list(after_smote.values()),
        marker_color=[TEAL_DARK, TEAL_LIGHT, CORAL],
        text=list(after_smote.values()),
        textposition='outside'
    )])
    fig.update_layout(
        title="After SMOTE — Balanced",
        plot_bgcolor='white', paper_bgcolor='white',
        height=400, font=dict(color="#2C3E3E"),
        yaxis=dict(title='Sample Count'),
        xaxis=dict(title='Class')
    )
    st.plotly_chart(fig, use_container_width=True)

# ============================================================
# SUMMARY TABLE
# ============================================================
st.markdown('<h3 class="section-header">Preprocessing Summary</h3>', unsafe_allow_html=True)

summary = pd.DataFrame({
    'Step': [f"{s['num']}. {s['title']}" for s in steps],
    'Purpose': [
        "Standardize missing-value representation",
        "Reduce dimensionality and noise",
        "Remove non-predictive and duplicate data",
        "Maintain dataset completeness",
        "Convert text to numerical form",
        "Enable supervised learning",
        "Normalize feature scales",
        "Handle class imbalance"
    ]
})

st.dataframe(summary, use_container_width=True, hide_index=True)
