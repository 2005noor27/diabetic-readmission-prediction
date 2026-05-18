"""
Page: Conclusion & Future Work
"""

import streamlit as st

st.set_page_config(page_title="Conclusion", page_icon="📝", layout="wide")

TEAL_DARK = "#2A6F6F"
TEAL_LIGHT = "#8AC4C4"
CORAL = "#D97757"

st.markdown("""
<style>
    .page-header {
        background: linear-gradient(135deg, #2A6F6F 0%, #4A9B9B 100%);
        padding: 2rem; border-radius: 12px;
        color: white; margin-bottom: 2rem;
    }
    .page-header h1 { color: white !important; margin: 0; }
    .page-header p { color: rgba(255,255,255,0.95); margin: 0.5rem 0 0 0; }
    
    .conclusion-box {
        background: white;
        padding: 1.8rem;
        border-radius: 10px;
        margin-bottom: 1.2rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    
    .conclusion-box h4 {
        color: #2A6F6F;
        margin-top: 0;
        border-bottom: 2px solid #8AC4C4;
        padding-bottom: 0.5rem;
    }
    
    .conclusion-box.coral {
        border-left: 4px solid #D97757;
    }
    
    .conclusion-box.teal {
        border-left: 4px solid #2A6F6F;
    }
    
    .conclusion-box.light {
        border-left: 4px solid #8AC4C4;
    }
    
    .section-header {
        color: #2A6F6F;
        font-weight: 600;
        margin-top: 2rem;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #8AC4C4;
    }
    
    ul li { color: #2C3E3E; line-height: 1.8; }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="page-header">
    <h1>📝 Conclusion & Future Work</h1>
    <p>Summary of findings, limitations, and directions for further research</p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# KEY FINDINGS
# ============================================================
st.markdown('<h3 class="section-header">Key Findings</h3>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="conclusion-box teal">
        <h4>🎯 Model Performance</h4>
        <p style="color:#2C3E3E; line-height:1.7;">
        Among the four classifiers tested, SVM with RBF kernel achieved the highest accuracy
        due to its ability to capture non-linear relationships in the clinical data. Decision Tree
        offered comparable performance with the added benefit of full interpretability — an
        important factor in medical applications.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="conclusion-box light">
        <h4>⚖️ Impact of SMOTE</h4>
        <p style="color:#2C3E3E; line-height:1.7;">
        Applying SMOTE significantly improved recall for the minority class (&lt;30 days
        readmission). Without it, models were heavily biased toward the majority class (NO),
        making them clinically useless for identifying at-risk patients.
        </p>
    </div>
    """, unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="conclusion-box coral">
        <h4>🔑 Most Predictive Features</h4>
        <p style="color:#2C3E3E; line-height:1.7;">
        The Random Forest importance analysis revealed that the strongest predictors of
        readmission are:
        </p>
        <ul style="padding-left:1.2rem;">
            <li>Number of lab procedures</li>
            <li>Number of medications</li>
            <li>Time spent in hospital</li>
            <li>Patient age</li>
            <li>Prior inpatient visits</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="conclusion-box teal">
        <h4>📐 Class Separability</h4>
        <p style="color:#2C3E3E; line-height:1.7;">
        The PCA 2D projection showed substantial overlap between the three readmission classes,
        suggesting that the problem is fundamentally difficult — patient outcomes depend on
        complex non-linear interactions that simple models struggle to capture.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# LIMITATIONS
# ============================================================
st.markdown('<h3 class="section-header">Limitations</h3>', unsafe_allow_html=True)

st.markdown("""
<div class="conclusion-box coral">
    <h4>What Could Be Improved</h4>
    <ul style="padding-left:1.2rem;">
        <li><b>Label Encoding on Nominal Data:</b> LabelEncoder imposes artificial ordering on nominal categorical features (e.g., race, medical specialty). OneHotEncoding would be more appropriate but increases dimensionality significantly.</li>
        <li><b>Information Loss from Outlier Removal:</b> The IQR-based outlier removal may have eliminated genuine clinical cases (e.g., very long hospital stays), reducing the model's ability to recognize unusual but real scenarios.</li>
        <li><b>Limited Hyperparameter Tuning:</b> Default or minimally tuned hyperparameters were used. Grid search or Bayesian optimization could improve results.</li>
        <li><b>Temporal Aspects Ignored:</b> The dataset spans 10 years but no time-based features (year, season, era of treatment guidelines) were engineered.</li>
        <li><b>Synthetic SMOTE Samples:</b> SMOTE creates artificial points that may not reflect realistic patient profiles, potentially introducing noise.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# ============================================================
# FUTURE WORK
# ============================================================
st.markdown('<h3 class="section-header">Future Work</h3>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="conclusion-box teal">
        <h4>🔬 Methodological Improvements</h4>
        <ul style="padding-left:1.2rem;">
            <li>Try Naive Bayes and MLP Neural Networks</li>
            <li>Use OneHotEncoder for nominal features</li>
            <li>Apply Grid Search or RandomizedSearch CV</li>
            <li>Use ensemble methods (XGBoost, LightGBM)</li>
            <li>Test alternative resampling methods (ADASYN, undersampling)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="conclusion-box light">
        <h4>🌐 Real-World Extensions</h4>
        <ul style="padding-left:1.2rem;">
            <li>Deploy as a clinical decision support tool</li>
            <li>Integrate with electronic health records</li>
            <li>Add explainability layer using SHAP or LIME</li>
            <li>Build a feedback loop with hospital outcomes</li>
            <li>Extend to other chronic diseases</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# FINAL TAKEAWAY
# ============================================================
st.markdown('<h3 class="section-header">Final Takeaway</h3>', unsafe_allow_html=True)

st.markdown("""
<div class="conclusion-box" style="background: linear-gradient(135deg, #F5F5F0 0%, #FFFFFF 100%); border-left: 4px solid #2A6F6F;">
    <p style="color:#2C3E3E; line-height:1.8; font-size:1.05rem; margin:0;">
    This project demonstrated the full pipeline of a Pattern Recognition workflow on a complex,
    real-world healthcare dataset. We learned that no single algorithm dominates — each has
    trade-offs between accuracy, interpretability, and computational cost. More importantly,
    we observed that <b>thoughtful preprocessing often matters more than choice of algorithm</b>.
    The class imbalance, missing data patterns, and feature engineering decisions had a much
    larger impact on results than switching between SVM and Logistic Regression.
    </p>
    <p style="color:#2C3E3E; line-height:1.8; font-size:1.05rem; margin-top:1rem; margin-bottom:0;">
    Pattern Recognition is not just about picking the "best" model — it's about understanding
    the data, the domain, and the consequences of getting predictions wrong. In healthcare,
    a false negative (missing a high-risk patient) costs far more than a false positive.
    Future work should prioritize <b>recall on the minority class</b> over raw accuracy.
    </p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# REFERENCES
# ============================================================
st.markdown('<h3 class="section-header">References</h3>', unsafe_allow_html=True)

st.markdown("""
<div class="conclusion-box">
    <ul style="padding-left:1.2rem;">
        <li>UCI Machine Learning Repository — Diabetes 130-US hospitals for years 1999-2008 Data Set</li>
        <li>Strack et al. (2014) — "Impact of HbA1c Measurement on Hospital Readmission Rates," BioMed Research International</li>
        <li>Pedregosa et al. (2011) — "Scikit-learn: Machine Learning in Python," JMLR</li>
        <li>Chawla et al. (2002) — "SMOTE: Synthetic Minority Over-sampling Technique," JAIR</li>
        <li>Breiman (2001) — "Random Forests," Machine Learning</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown(
    '<p style="text-align:center; color:#6B7878; font-size:0.9rem;">'
    '<b>Pattern Recognition Project · DA360 · Yarmouk University · 2026</b>'
    '</p>',
    unsafe_allow_html=True
)
