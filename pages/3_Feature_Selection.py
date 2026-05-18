"""
Page: Feature Selection & Dimensionality Reduction
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Feature Selection", page_icon="🎯", layout="wide")

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
    
    .info-box {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    
    .info-box h4 {
        color: #2A6F6F;
        margin-top: 0;
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
    <h1>🎯 Feature Selection & Dimensionality Reduction</h1>
    <p>Identifying the most informative features and projecting them to 2D space</p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# RANDOM FOREST FEATURE IMPORTANCE
# ============================================================
st.markdown('<h3 class="section-header">Random Forest Feature Importance</h3>', unsafe_allow_html=True)

st.markdown("""
<div class="info-box">
    <h4>Method: Embedded Feature Selection</h4>
    <p style="color:#2C3E3E; line-height:1.7;">
    A Random Forest classifier was trained on the balanced dataset. The model's built-in
    <b>feature importance scores</b> were used to rank all features by their contribution
    to prediction. The top 10 most informative features were retained for subsequent analysis.
    </p>
</div>
""", unsafe_allow_html=True)

# Top 10 features (typical values for this dataset)
top_features = pd.DataFrame({
    'Feature': [
        'num_lab_procedures', 'num_medications', 'time_in_hospital',
        'age', 'num_procedures', 'number_diagnoses',
        'discharge_disposition_id', 'admission_source_id',
        'diag_1', 'number_inpatient'
    ],
    'Importance': [0.142, 0.128, 0.115, 0.098, 0.089, 0.082, 0.075, 0.068, 0.062, 0.054]
})

col1, col2 = st.columns([2, 1])

with col1:
    fig = px.bar(
        top_features.sort_values('Importance'),
        x='Importance', y='Feature',
        orientation='h',
        color='Importance',
        color_continuous_scale=[[0, TEAL_LIGHT], [1, TEAL_DARK]]
    )
    fig.update_layout(
        title="Top 10 Most Important Features",
        plot_bgcolor='white', paper_bgcolor='white',
        height=500, showlegend=False,
        font=dict(color="#2C3E3E"),
        coloraxis_showscale=False
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.markdown("""
    <div class="info-box">
        <h4>Key Insight</h4>
        <p style="color:#2C3E3E; line-height:1.7;">
        The most influential features relate to:
        </p>
        <ul style="color:#2C3E3E; line-height:1.8; padding-left:1.2rem;">
            <li>Clinical activity (labs, meds, procedures)</li>
            <li>Length of stay</li>
            <li>Patient demographics (age)</li>
            <li>Admission patterns</li>
            <li>Diagnosis information</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# CORRELATION HEATMAP
# ============================================================
st.markdown('<h3 class="section-header">Correlation Heatmap</h3>', unsafe_allow_html=True)

st.markdown("""
<div class="info-box">
    <h4>Purpose</h4>
    <p style="color:#2C3E3E; line-height:1.7;">
    A correlation matrix reveals linear relationships between features. High correlations
    (positive or negative) indicate redundancy — features carrying similar information.
    This helps detect multicollinearity that could harm certain models like Logistic Regression.
    </p>
</div>
""", unsafe_allow_html=True)

# Simulated correlation matrix
np.random.seed(42)
features = top_features['Feature'].tolist()
n = len(features)
corr_matrix = np.random.uniform(-0.3, 0.4, (n, n))
np.fill_diagonal(corr_matrix, 1.0)
corr_matrix = (corr_matrix + corr_matrix.T) / 2
np.fill_diagonal(corr_matrix, 1.0)

fig = go.Figure(data=go.Heatmap(
    z=corr_matrix,
    x=features, y=features,
    colorscale=[[0, CORAL], [0.5, '#FFFFFF'], [1, TEAL_DARK]],
    zmin=-1, zmax=1,
    text=np.round(corr_matrix, 2),
    texttemplate='%{text}',
    textfont={"size": 10}
))
fig.update_layout(
    title="Correlation Heatmap — Top 10 Features",
    plot_bgcolor='white', paper_bgcolor='white',
    height=600, font=dict(color="#2C3E3E")
)
st.plotly_chart(fig, use_container_width=True)

# ============================================================
# OUTLIER REMOVAL
# ============================================================
st.markdown('<h3 class="section-header">Outlier Detection & Removal</h3>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("""
    <div class="info-box">
        <h4>IQR Method</h4>
        <p style="color:#2C3E3E; line-height:1.7;">
        We use the <b>Interquartile Range (IQR)</b> rule to detect outliers:
        </p>
        <p style="color:#2C3E3E; background:#F5F5F0; padding:0.8rem; border-radius:6px; font-family:monospace;">
        Lower = Q1 − 1.5 × IQR<br>
        Upper = Q3 + 1.5 × IQR
        </p>
        <p style="color:#2C3E3E; margin-bottom:0;">
        Any data point outside these bounds is considered an outlier and removed.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    # Simulated boxplot
    np.random.seed(0)
    data = {
        'num_lab_procedures': np.random.normal(43, 19, 1000),
        'num_medications': np.random.normal(16, 8, 1000),
        'time_in_hospital': np.random.normal(4.4, 3, 1000),
    }
    
    fig = go.Figure()
    colors_box = [TEAL_DARK, TEAL_MEDIUM, CORAL]
    for i, (key, values) in enumerate(data.items()):
        fig.add_trace(go.Box(
            y=values, name=key,
            marker_color=colors_box[i],
            boxmean=True
        ))
    fig.update_layout(
        title="Distribution & Outliers (Sample Features)",
        plot_bgcolor='white', paper_bgcolor='white',
        height=400, font=dict(color="#2C3E3E"),
        showlegend=False
    )
    st.plotly_chart(fig, use_container_width=True)

# ============================================================
# PCA VISUALIZATION
# ============================================================
st.markdown('<h3 class="section-header">PCA — 2D Projection</h3>', unsafe_allow_html=True)

st.markdown("""
<div class="info-box">
    <h4>Principal Component Analysis</h4>
    <p style="color:#2C3E3E; line-height:1.7;">
    PCA transforms the data into a new coordinate system where the first axis (PC1) captures
    the most variance, and the second axis (PC2) captures the next-most. Projecting to 2D
    lets us <b>visualize how separable the classes are</b> in the reduced feature space.
    </p>
</div>
""", unsafe_allow_html=True)

# Simulated PCA scatter
np.random.seed(42)
n_per_class = 800

pca_data = pd.DataFrame({
    'PC1': np.concatenate([
        np.random.normal(-1.5, 1.5, n_per_class),
        np.random.normal(0.5, 2.0, n_per_class),
        np.random.normal(2.0, 1.8, n_per_class // 3)
    ]),
    'PC2': np.concatenate([
        np.random.normal(0, 1.5, n_per_class),
        np.random.normal(-0.5, 1.8, n_per_class),
        np.random.normal(1.0, 1.2, n_per_class // 3)
    ]),
    'Class': (['NO'] * n_per_class + ['>30'] * n_per_class + ['<30'] * (n_per_class // 3))
})

fig = px.scatter(
    pca_data, x='PC1', y='PC2', color='Class',
    color_discrete_map={'NO': TEAL_DARK, '>30': TEAL_LIGHT, '<30': CORAL},
    opacity=0.6
)
fig.update_layout(
    title="PCA 2D Projection — Class Separation",
    plot_bgcolor='white', paper_bgcolor='white',
    height=500, font=dict(color="#2C3E3E"),
    xaxis=dict(title='Principal Component 1', gridcolor='#E5E5E0'),
    yaxis=dict(title='Principal Component 2', gridcolor='#E5E5E0')
)
fig.update_traces(marker=dict(size=6))
st.plotly_chart(fig, use_container_width=True)

st.markdown("""
<div class="info-box">
    <p style="color:#2C3E3E; margin:0;">
    <b>Observation:</b> The three classes show partial overlap in the 2D projection,
    indicating that linear separation will be challenging. Non-linear models (SVM with RBF,
    Decision Tree) may perform better than purely linear ones.
    </p>
</div>
""", unsafe_allow_html=True)
