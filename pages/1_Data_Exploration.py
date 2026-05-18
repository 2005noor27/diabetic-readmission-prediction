"""
Page: Data Exploration
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(page_title="Data Exploration", page_icon="📊", layout="wide")

# ============================================================
# THEME COLORS
# ============================================================
TEAL_DARK = "#2A6F6F"
TEAL_MEDIUM = "#4A9B9B"
TEAL_LIGHT = "#8AC4C4"
CORAL = "#D97757"
GRAY = "#A8A8A8"
BG = "#F5F5F0"

# ============================================================
# CUSTOM CSS
# ============================================================
st.markdown("""
<style>
    .page-header {
        background: linear-gradient(135deg, #2A6F6F 0%, #4A9B9B 100%);
        padding: 2rem;
        border-radius: 12px;
        color: white;
        margin-bottom: 2rem;
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

# ============================================================
# HEADER
# ============================================================
st.markdown("""
<div class="page-header">
    <h1>📊 Data Exploration</h1>
    <p>Understanding the structure and characteristics of the dataset</p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# LOAD DATA
# ============================================================
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("diabetic_data.csv")
        return df
    except FileNotFoundError:
        st.error("⚠️ diabetic_data.csv not found. Please place it in the project root folder.")
        return None

df = load_data()

if df is None:
    st.stop()

# ============================================================
# OVERVIEW METRICS
# ============================================================
st.markdown('<h3 class="section-header">Dataset Overview</h3>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Records", f"{len(df):,}")
with col2:
    st.metric("Features", f"{df.shape[1]}")
with col3:
    missing_pct = (df.replace("?", np.nan).isnull().sum().sum() / (df.shape[0] * df.shape[1])) * 100
    st.metric("Missing Data", f"{missing_pct:.1f}%")
with col4:
    st.metric("Unique Patients", f"{df['patient_nbr'].nunique():,}")

# ============================================================
# DATA PREVIEW
# ============================================================
st.markdown('<h3 class="section-header">Data Preview</h3>', unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["📋 Sample Records", "📐 Column Types", "🔍 Missing Values"])

with tab1:
    st.dataframe(df.head(20), use_container_width=True, height=400)

with tab2:
    dtype_df = pd.DataFrame({
        'Column': df.columns,
        'Type': df.dtypes.astype(str),
        'Unique Values': [df[col].nunique() for col in df.columns],
        'Sample': [df[col].iloc[0] for col in df.columns]
    })
    st.dataframe(dtype_df, use_container_width=True, height=400)

with tab3:
    df_check = df.replace("?", np.nan)
    missing = df_check.isnull().sum()
    missing = missing[missing > 0].sort_values(ascending=False)
    
    if len(missing) > 0:
        miss_df = pd.DataFrame({
            'Column': missing.index,
            'Missing Count': missing.values,
            'Missing %': (missing.values / len(df) * 100).round(2)
        })
        
        fig = px.bar(
            miss_df, x='Missing %', y='Column',
            orientation='h',
            color='Missing %',
            color_continuous_scale=[[0, TEAL_LIGHT], [0.5, TEAL_MEDIUM], [1, CORAL]]
        )
        fig.update_layout(
            plot_bgcolor='white', paper_bgcolor='white',
            height=400, showlegend=False,
            font=dict(color="#2C3E3E")
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.success("No missing values detected!")

# ============================================================
# TARGET DISTRIBUTION
# ============================================================
st.markdown('<h3 class="section-header">Target Variable Distribution</h3>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    target_counts = df['readmitted'].value_counts()
    
    fig = go.Figure(data=[go.Pie(
        labels=target_counts.index,
        values=target_counts.values,
        hole=0.5,
        marker=dict(colors=[TEAL_DARK, TEAL_LIGHT, CORAL]),
        textfont=dict(size=14, color='white')
    )])
    fig.update_layout(
        title="Readmission Class Distribution",
        paper_bgcolor='white',
        height=400,
        font=dict(color="#2C3E3E")
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig = px.bar(
        x=target_counts.index, y=target_counts.values,
        labels={'x': 'Readmission', 'y': 'Count'},
        color=target_counts.index,
        color_discrete_map={'NO': TEAL_DARK, '>30': TEAL_LIGHT, '<30': CORAL}
    )
    fig.update_layout(
        title="Class Counts",
        plot_bgcolor='white', paper_bgcolor='white',
        height=400, showlegend=False,
        font=dict(color="#2C3E3E")
    )
    st.plotly_chart(fig, use_container_width=True)

st.markdown(f"""
<div class="info-box">
    <p style="color:#2C3E3E; margin:0;">
    <b>Class Imbalance Observed:</b> The majority of patients ({target_counts.iloc[0]:,}) were not readmitted (NO),
    while only {target_counts.get('<30', 0):,} were readmitted within 30 days.
    This imbalance must be addressed using techniques like SMOTE during preprocessing.
    </p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# DEMOGRAPHICS
# ============================================================
st.markdown('<h3 class="section-header">Patient Demographics</h3>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    age_counts = df['age'].value_counts().sort_index()
    fig = px.bar(
        x=age_counts.index, y=age_counts.values,
        labels={'x': 'Age Group', 'y': 'Count'},
        color_discrete_sequence=[TEAL_DARK]
    )
    fig.update_layout(
        title="Age Distribution",
        plot_bgcolor='white', paper_bgcolor='white',
        height=350, font=dict(color="#2C3E3E")
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    gender_counts = df['gender'].value_counts()
    fig = px.pie(
        values=gender_counts.values, names=gender_counts.index,
        color_discrete_sequence=[TEAL_DARK, CORAL, GRAY]
    )
    fig.update_layout(
        title="Gender Distribution",
        paper_bgcolor='white', height=350,
        font=dict(color="#2C3E3E")
    )
    st.plotly_chart(fig, use_container_width=True)

# Race
race_counts = df['race'].value_counts()
fig = px.bar(
    x=race_counts.values, y=race_counts.index,
    orientation='h',
    labels={'x': 'Count', 'y': 'Race'},
    color=race_counts.values,
    color_continuous_scale=[[0, TEAL_LIGHT], [1, TEAL_DARK]]
)
fig.update_layout(
    title="Race Distribution",
    plot_bgcolor='white', paper_bgcolor='white',
    height=350, showlegend=False,
    font=dict(color="#2C3E3E")
)
st.plotly_chart(fig, use_container_width=True)

# ============================================================
# READMISSION BY AGE
# ============================================================
st.markdown('<h3 class="section-header">Readmission by Age Group</h3>', unsafe_allow_html=True)

age_readmit = df.groupby(['age', 'readmitted']).size().reset_index(name='count')

fig = px.bar(
    age_readmit, x='age', y='count', color='readmitted',
    color_discrete_map={'NO': TEAL_DARK, '>30': TEAL_LIGHT, '<30': CORAL},
    labels={'count': 'Number of Patients', 'age': 'Age Group'}
)
fig.update_layout(
    title="Readmission Distribution Across Age Groups",
    plot_bgcolor='white', paper_bgcolor='white',
    height=450, font=dict(color="#2C3E3E"),
    barmode='stack'
)
st.plotly_chart(fig, use_container_width=True)

# ============================================================
# NUMERICAL FEATURES
# ============================================================
st.markdown('<h3 class="section-header">Numerical Features Distribution</h3>', unsafe_allow_html=True)

num_features = ['time_in_hospital', 'num_lab_procedures', 'num_procedures',
                'num_medications', 'number_diagnoses']

selected_feat = st.selectbox("Select a numerical feature to visualize:", num_features)

col1, col2 = st.columns(2)

with col1:
    fig = px.histogram(
        df, x=selected_feat,
        color_discrete_sequence=[TEAL_DARK],
        nbins=30
    )
    fig.update_layout(
        title=f"Distribution of {selected_feat}",
        plot_bgcolor='white', paper_bgcolor='white',
        height=400, font=dict(color="#2C3E3E")
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig = px.box(
        df, x='readmitted', y=selected_feat,
        color='readmitted',
        color_discrete_map={'NO': TEAL_DARK, '>30': TEAL_LIGHT, '<30': CORAL}
    )
    fig.update_layout(
        title=f"{selected_feat} by Readmission Class",
        plot_bgcolor='white', paper_bgcolor='white',
        height=400, font=dict(color="#2C3E3E"),
        showlegend=False
    )
    st.plotly_chart(fig, use_container_width=True)
