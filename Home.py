"""
Diabetic Patient Readmission Prediction
Pattern Recognition Project - DA360
Yarmouk University
"""

import streamlit as st

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="Diabetic Readmission Prediction",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM CSS
# ============================================================
st.markdown("""
<style>
    /* Main container */
    .main {
        background-color: #F5F5F0;
    }
    
    /* Hero header */
    .hero {
        background: linear-gradient(135deg, #2A6F6F 0%, #4A9B9B 100%);
        padding: 3rem 2rem;
        border-radius: 12px;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 4px 12px rgba(42, 111, 111, 0.15);
    }
    
    .hero h1 {
        color: white !important;
        margin: 0;
        font-size: 2.5rem;
        font-weight: 700;
    }
    
    .hero p {
        color: rgba(255,255,255,0.95);
        margin-top: 0.5rem;
        font-size: 1.1rem;
    }
    
    /* Metric cards */
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #2A6F6F;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        height: 100%;
    }
    
    .metric-card.coral {
        border-left-color: #D97757;
    }
    
    .metric-card.teal-light {
        border-left-color: #8AC4C4;
    }
    
    .metric-label {
        color: #6B7878;
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 0.5rem;
    }
    
    .metric-value {
        color: #2C3E3E;
        font-size: 2rem;
        font-weight: 700;
        margin: 0;
    }
    
    .metric-sub {
        color: #6B7878;
        font-size: 0.9rem;
        margin-top: 0.3rem;
    }
    
    /* Section headers */
    .section-header {
        color: #2A6F6F;
        font-weight: 600;
        margin-top: 2rem;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #8AC4C4;
    }
    
    /* Info boxes */
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
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #FFFFFF;
        border-right: 1px solid #E5E5E0;
    }
    
    /* Hide default streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Custom button */
    .stButton > button {
        background: #2A6F6F;
        color: white;
        border: none;
        padding: 0.6rem 1.5rem;
        border-radius: 8px;
        font-weight: 500;
        transition: all 0.2s;
    }
    
    .stButton > button:hover {
        background: #4A9B9B;
        color: white;
        transform: translateY(-1px);
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# SIDEBAR
# ============================================================
with st.sidebar:
    st.markdown("### 🏥 Project Navigation")
    st.markdown("---")
    st.markdown("""
    **Pattern Recognition Project**  
    Course: DA360  
    Yarmouk University
    """)
    st.markdown("---")
    st.markdown("#### 📋 Team Members")
    st.markdown("""
    - Member 1  
    - Member 2  
    - Member 3
    """)
    st.markdown("---")
    st.caption("Use the pages above to navigate through the project sections.")

# ============================================================
# HERO SECTION
# ============================================================
st.markdown("""
<div class="hero">
    <h1>🏥 Diabetic Patient Readmission Prediction</h1>
    <p>Applying Pattern Recognition Techniques to Predict Hospital Readmission</p>
    <p style="margin-top:1rem; font-size:0.95rem; opacity:0.9;">
        Pattern Recognition (DA360) · Yarmouk University
    </p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# KEY METRICS
# ============================================================
st.markdown('<h3 class="section-header">Project at a Glance</h3>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Dataset Size</div>
        <p class="metric-value">101,766</p>
        <div class="metric-sub">Patient records</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card coral">
        <div class="metric-label">Features</div>
        <p class="metric-value">50</p>
        <div class="metric-sub">Clinical attributes</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card teal-light">
        <div class="metric-label">Target Classes</div>
        <p class="metric-value">3</p>
        <div class="metric-sub">NO, &lt;30, &gt;30 days</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Models Trained</div>
        <p class="metric-value">4</p>
        <div class="metric-sub">Classification algorithms</div>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# PROBLEM STATEMENT
# ============================================================
st.markdown('<h3 class="section-header">Problem Statement</h3>', unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    <div class="info-box">
        <h4>Why Hospital Readmission Matters</h4>
        <p style="color:#2C3E3E; line-height:1.7;">
        Hospital readmission of diabetic patients is a major concern in healthcare systems worldwide.
        Frequent readmissions indicate gaps in patient care, increase healthcare costs significantly,
        and reduce quality of life for patients. By identifying patients at high risk of readmission,
        hospitals can take preventive measures and personalize follow-up care.
        </p>
        <p style="color:#2C3E3E; line-height:1.7; margin-bottom:0;">
        This project applies <b>Pattern Recognition</b> techniques to predict whether a diabetic
        patient will be readmitted, and if so, within what timeframe.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-box">
        <h4>Objectives</h4>
        <ul style="color:#2C3E3E; line-height:1.9; padding-left:1.2rem;">
            <li>Apply PR techniques on a real-world dataset</li>
            <li>Compare multiple classifiers</li>
            <li>Visualize feature spaces and results</li>
            <li>Build an interpretable prediction system</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# WORKFLOW
# ============================================================
st.markdown('<h3 class="section-header">Project Workflow</h3>', unsafe_allow_html=True)

st.markdown("""
<div class="info-box">
    <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:1rem;">
        <div style="text-align:center; flex:1; min-width:120px;">
            <div style="background:#2A6F6F; color:white; width:50px; height:50px; border-radius:50%; 
                        display:flex; align-items:center; justify-content:center; margin:0 auto 0.5rem; 
                        font-weight:600; font-size:1.2rem;">1</div>
            <strong style="color:#2C3E3E;">Data Exploration</strong>
        </div>
        <div style="color:#8AC4C4; font-size:1.5rem;">→</div>
        <div style="text-align:center; flex:1; min-width:120px;">
            <div style="background:#4A9B9B; color:white; width:50px; height:50px; border-radius:50%; 
                        display:flex; align-items:center; justify-content:center; margin:0 auto 0.5rem; 
                        font-weight:600; font-size:1.2rem;">2</div>
            <strong style="color:#2C3E3E;">Preprocessing</strong>
        </div>
        <div style="color:#8AC4C4; font-size:1.5rem;">→</div>
        <div style="text-align:center; flex:1; min-width:120px;">
            <div style="background:#8AC4C4; color:white; width:50px; height:50px; border-radius:50%; 
                        display:flex; align-items:center; justify-content:center; margin:0 auto 0.5rem; 
                        font-weight:600; font-size:1.2rem;">3</div>
            <strong style="color:#2C3E3E;">Feature Selection</strong>
        </div>
        <div style="color:#8AC4C4; font-size:1.5rem;">→</div>
        <div style="text-align:center; flex:1; min-width:120px;">
            <div style="background:#D97757; color:white; width:50px; height:50px; border-radius:50%; 
                        display:flex; align-items:center; justify-content:center; margin:0 auto 0.5rem; 
                        font-weight:600; font-size:1.2rem;">4</div>
            <strong style="color:#2C3E3E;">Model Training</strong>
        </div>
        <div style="color:#8AC4C4; font-size:1.5rem;">→</div>
        <div style="text-align:center; flex:1; min-width:120px;">
            <div style="background:#2A6F6F; color:white; width:50px; height:50px; border-radius:50%; 
                        display:flex; align-items:center; justify-content:center; margin:0 auto 0.5rem; 
                        font-weight:600; font-size:1.2rem;">5</div>
            <strong style="color:#2C3E3E;">Live Prediction</strong>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================================
# DATASET INFO
# ============================================================
st.markdown('<h3 class="section-header">Dataset Information</h3>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="info-box">
        <h4>📊 Source & Origin</h4>
        <p style="color:#2C3E3E;"><b>Name:</b> Diabetes 130-US Hospitals (1999–2008)</p>
        <p style="color:#2C3E3E;"><b>Repository:</b> UCI Machine Learning Repository</p>
        <p style="color:#2C3E3E;"><b>Type:</b> Multiclass Classification</p>
        <p style="color:#2C3E3E; margin-bottom:0;"><b>Domain:</b> Healthcare / Clinical Records</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-box">
        <h4>🎯 Target Variable</h4>
        <p style="color:#2C3E3E;"><b>readmitted</b> — three possible outcomes:</p>
        <ul style="color:#2C3E3E; line-height:1.8; padding-left:1.2rem;">
            <li><b>NO</b> — Patient was not readmitted</li>
            <li><b>&lt;30</b> — Readmitted within 30 days</li>
            <li><b>&gt;30</b> — Readmitted after 30 days</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# FOOTER
# ============================================================
st.markdown("---")
st.markdown(
    '<p style="text-align:center; color:#6B7878; font-size:0.85rem;">'
    'Pattern Recognition Project · DA360 · Yarmouk University · 2026'
    '</p>',
    unsafe_allow_html=True
)
