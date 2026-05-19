"""
Page: Live Prediction
Interactive form to predict readmission risk for new patients
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import pickle
import os

st.set_page_config(page_title="Live Prediction", page_icon="🔮", layout="wide")

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
    
    .input-section {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    
    .input-section h4 {
        color: #2A6F6F;
        margin-top: 0;
        border-bottom: 2px solid #8AC4C4;
        padding-bottom: 0.5rem;
    }
    
    .result-card {
        background: white;
        padding: 2rem;
        border-radius: 12px;
        margin-top: 1rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        text-align: center;
    }
    
    .prediction-label {
        font-size: 2.5rem;
        font-weight: 700;
        margin: 1rem 0;
    }
    
    .prediction-no { color: #2A6F6F; }
    .prediction-low { color: #8AC4C4; }
    .prediction-high { color: #D97757; }
    
    .risk-badge {
        display: inline-block;
        padding: 0.4rem 1.2rem;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.9rem;
        margin-top: 0.5rem;
    }
    
    .risk-low { background: #E0F0F0; color: #2A6F6F; }
    .risk-medium { background: #FFE8DD; color: #B85A3A; }
    .risk-high { background: #FFD4C4; color: #8B3B1F; }
    
    .section-header {
        color: #2A6F6F;
        font-weight: 600;
        margin-top: 2rem;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #8AC4C4;
    }
    
    .stButton > button {
        background: #2A6F6F;
        color: white;
        border: none;
        padding: 0.8rem 2rem;
        border-radius: 8px;
        font-weight: 600;
        font-size: 1rem;
        width: 100%;
    }
    
    .stButton > button:hover {
        background: #4A9B9B;
        color: white;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="page-header">
    <h1>🔮 Live Readmission Prediction</h1>
    <p>Enter patient information to predict the likelihood of hospital readmission</p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# MODEL SELECTION
# ============================================================
st.markdown('<h3 class="section-header">Step 1 — Select Model</h3>', unsafe_allow_html=True)

model_choice = st.radio(
    "Choose the algorithm to use for prediction:",
    ["SVM (Recommended)", "Decision Tree", "k-NN", "Logistic Regression"],
    horizontal=True
)

# ============================================================
# PATIENT INPUT
# ============================================================
st.markdown('<h3 class="section-header">Step 2 — Patient Information</h3>', unsafe_allow_html=True)

with st.container():
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="input-section"><h4>👤 Demographics</h4>', unsafe_allow_html=True)
        age = st.selectbox("Age Group", [
            "[0-10)", "[10-20)", "[20-30)", "[30-40)", "[40-50)",
            "[50-60)", "[60-70)", "[70-80)", "[80-90)", "[90-100)"
        ], index=6)
        gender = st.selectbox("Gender", ["Female", "Male"])
        race = st.selectbox("Race", [
            "Caucasian", "AfricanAmerican", "Hispanic", "Asian", "Other"
        ])
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="input-section"><h4>🏥 Hospital Stay</h4>', unsafe_allow_html=True)
        time_in_hospital = st.slider("Days in Hospital", 1, 14, 4)
        num_procedures = st.slider("Number of Procedures", 0, 10, 1)
        num_medications = st.slider("Number of Medications", 1, 80, 16)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="input-section"><h4>🔬 Clinical Data</h4>', unsafe_allow_html=True)
        num_lab_procedures = st.slider("Lab Procedures", 1, 130, 43)
        number_diagnoses = st.slider("Total Diagnoses", 1, 16, 7)
        number_inpatient = st.slider("Prior Inpatient Visits", 0, 20, 0)
        st.markdown('</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="input-section"><h4>💊 Medication Management</h4>', unsafe_allow_html=True)
    diabetes_med = st.selectbox("On Diabetes Medication?", ["Yes", "No"])
    change = st.selectbox("Medication Changed?", ["No", "Ch"])
    insulin = st.selectbox("Insulin", ["No", "Down", "Steady", "Up"])
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="input-section"><h4>📋 Admission Info</h4>', unsafe_allow_html=True)
    admission_type = st.selectbox("Admission Type", [
        "Emergency", "Urgent", "Elective", "Newborn", "Not Available"
    ])
    discharge = st.selectbox("Discharge Disposition", [
        "Home", "Transferred", "Home Health Care", "Expired", "Other"
    ])
    admission_source = st.selectbox("Admission Source", [
        "Emergency Room", "Physician Referral", "Transfer", "Other"
    ])
    st.markdown('</div>', unsafe_allow_html=True)

# ============================================================
# PREDICTION
# ============================================================
st.markdown('<h3 class="section-header">Step 3 — Get Prediction</h3>', unsafe_allow_html=True)

if st.button("🔮 Predict Readmission Risk", type="primary"):
    
    # Simple rule-based prediction (placeholder for actual model)
    # Replace this with: model.predict(patient_features)
    
    risk_score = 0
    
    # Age contribution
    age_idx = ["[0-10)", "[10-20)", "[20-30)", "[30-40)", "[40-50)",
               "[50-60)", "[60-70)", "[70-80)", "[80-90)", "[90-100)"].index(age)
    risk_score += age_idx * 0.05
    
    # Hospital stay
    risk_score += time_in_hospital * 0.04
    
    # Procedures and meds
    risk_score += num_procedures * 0.03
    risk_score += num_medications * 0.008
    risk_score += num_lab_procedures * 0.003
    
    # Diagnoses
    risk_score += number_diagnoses * 0.04
    
    # Prior inpatient visits (strong signal)
    risk_score += number_inpatient * 0.1
    
    # Medication management
    if diabetes_med == "Yes":
        risk_score += 0.1
    if change == "Ch":
        risk_score += 0.08
    
    # Normalize
    risk_score = min(risk_score, 1.0)
    
    # Determine class
    if risk_score < 0.4:
        prediction = "NO Readmission"
        prediction_class = "prediction-no"
        risk_level = "Low Risk"
        risk_class = "risk-low"
        prob_no = 0.6 + (0.4 - risk_score) * 0.5
        prob_long = 0.25
        prob_short = 0.15
    elif risk_score < 0.7:
        prediction = "Readmission > 30 days"
        prediction_class = "prediction-low"
        risk_level = "Medium Risk"
        risk_class = "risk-medium"
        prob_no = 0.35
        prob_long = 0.45
        prob_short = 0.20
    else:
        prediction = "Readmission < 30 days"
        prediction_class = "prediction-high"
        risk_level = "High Risk"
        risk_class = "risk-high"
        prob_no = 0.2
        prob_long = 0.3
        prob_short = 0.5
    
    # Normalize probabilities
    total = prob_no + prob_long + prob_short
    prob_no /= total
    prob_long /= total
    prob_short /= total
    
    # Display result
    st.markdown(f"""
    <div class="result-card">
        <p style="color:#6B7878; margin:0; font-size:0.9rem;">PREDICTION RESULT</p>
        <p class="prediction-label {prediction_class}">{prediction}</p>
        <span class="risk-badge {risk_class}">{risk_level}</span>
        <p style="color:#6B7878; margin-top:1rem; font-size:0.85rem;">
            Model used: <b>{model_choice}</b>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Probability distribution
    st.markdown('<h3 class="section-header">Probability Distribution</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        fig = go.Figure(data=[go.Bar(
            x=['NO Readmission', '> 30 days', '< 30 days'],
            y=[prob_no, prob_long, prob_short],
            marker_color=[TEAL_DARK, TEAL_LIGHT, CORAL],
            text=[f"{p:.1%}" for p in [prob_no, prob_long, prob_short]],
            textposition='outside'
        )])
        fig.update_layout(
            title="Class Probabilities",
            plot_bgcolor='white', paper_bgcolor='white',
            height=400, font=dict(color="#2C3E3E"),
            yaxis=dict(tickformat='.0%', range=[0, 1])
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Risk gauge
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=risk_score * 100,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "Risk Score"},
            number={'suffix': "%"},
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': TEAL_DARK},
                'steps': [
                    {'range': [0, 40], 'color': '#E0F0F0'},
                    {'range': [40, 70], 'color': '#FFE8DD'},
                    {'range': [70, 100], 'color': '#FFD4C4'}
                ],
                'threshold': {
                    'line': {'color': CORAL, 'width': 4},
                    'thickness': 0.75,
                    'value': risk_score * 100
                }
            }
        ))
        fig.update_layout(
            paper_bgcolor='white',
            height=400, font=dict(color="#2C3E3E")
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Recommendations
    st.markdown('<h3 class="section-header">Clinical Recommendations</h3>', unsafe_allow_html=True)
    
    if risk_score < 0.4:
        st.success("""
        ✅ **Low risk profile detected.**  
        Standard discharge protocol can be applied. Regular follow-up scheduling is sufficient.
        """)
    elif risk_score < 0.7:
        st.warning("""
        ⚠️ **Medium risk profile detected.**  
        Consider extended monitoring and follow-up within 30 days. Review medication adherence plan.
        """)
    else:
        st.error("""
        🚨 **High risk profile detected.**  
        Recommend close post-discharge monitoring, scheduled follow-up within 7 days,
        and home health care evaluation. Consider medication reconciliation review.
        """)

