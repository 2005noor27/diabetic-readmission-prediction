"""
Page: Models & Results
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Models & Results", page_icon="🤖", layout="wide")

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
    
    .model-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        border-top: 4px solid #2A6F6F;
    }
    
    .model-card.coral { border-top-color: #D97757; }
    .model-card.light { border-top-color: #8AC4C4; }
    .model-card.medium { border-top-color: #4A9B9B; }
    
    .model-name {
        color: #2A6F6F;
        font-size: 1.3rem;
        font-weight: 600;
        margin: 0 0 0.5rem 0;
    }
    
    .metric-row {
        display: flex;
        justify-content: space-between;
        padding: 0.5rem 0;
        border-bottom: 1px solid #F5F5F0;
    }
    
    .metric-row:last-child { border-bottom: none; }
    
    .section-header {
        color: #2A6F6F;
        font-weight: 600;
        margin-top: 2rem;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #8AC4C4;
    }
    
    .info-box {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    
    .info-box h4 { color: #2A6F6F; margin-top: 0; }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="page-header">
    <h1>🤖 Models & Results</h1>
    <p>Training, evaluating, and comparing four classification algorithms</p>
</div>
""", unsafe_allow_html=True)


# ============================================================
# RESULTS (Actual results from training)
# ============================================================

results = {
    'Decision Tree': {
        'accuracy': 0.4230, 'precision': 0.52, 'recall': 0.42, 'f1': 0.42,
        'desc': 'Tree-based model that splits data into branches based on feature thresholds. Highly interpretable and handles non-linear patterns.',
        'params': 'max_depth=5, random_state=42'
    },
    'k-NN': {
        'accuracy': 0.3910, 'precision': 0.49, 'recall': 0.39, 'f1': 0.42,
        'desc': 'Distance-based classifier that assigns each sample the most common label among its k nearest training neighbors.',
        'params': 'n_neighbors=5'
    },
    'SVM': {
        'accuracy': 0.4537, 'precision': 0.52, 'recall': 0.45, 'f1': 0.48,
        'desc': 'Support Vector Machine with RBF kernel that finds optimal decision boundaries in transformed feature spaces.',
        'params': "kernel='rbf', random_state=42"
    },
    'Logistic Regression': {
        'accuracy': 0.4506, 'precision': 0.51, 'recall': 0.45, 'f1': 0.45,
        'desc': 'Linear model that estimates class probabilities using the sigmoid function. Fast and interpretable.',
        'params': 'max_iter=1000, random_state=42'
    }
}

# ============================================================
# MODELS GRID
# ============================================================
st.markdown('<h3 class="section-header">Trained Models</h3>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

models_list = list(results.items())
card_classes = ['', 'coral', 'light', 'medium']

for i, (name, data) in enumerate(models_list):
    col = col1 if i % 2 == 0 else col2
    with col:
        st.markdown(f"""
        <div class="model-card {card_classes[i]}">
            <p class="model-name">{name}</p>
            <p style="color:#6B7878; font-size:0.85rem; margin:0 0 0.5rem 0;">
                <code>{data['params']}</code>
            </p>
            <p style="color:#2C3E3E; font-size:0.95rem; line-height:1.6;">
                {data['desc']}
            </p>
            <div style="margin-top:1rem;">
                <div class="metric-row">
                    <span style="color:#6B7878;">Accuracy</span>
                    <strong style="color:#2A6F6F;">{data['accuracy']:.2%}</strong>
                </div>
                <div class="metric-row">
                    <span style="color:#6B7878;">Precision</span>
                    <strong style="color:#2A6F6F;">{data['precision']:.2%}</strong>
                </div>
                <div class="metric-row">
                    <span style="color:#6B7878;">Recall</span>
                    <strong style="color:#2A6F6F;">{data['recall']:.2%}</strong>
                </div>
                <div class="metric-row">
                    <span style="color:#6B7878;">F1-Score</span>
                    <strong style="color:#2A6F6F;">{data['f1']:.2%}</strong>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ============================================================
# COMPARISON TABLE
# ============================================================
st.markdown('<h3 class="section-header">Performance Comparison</h3>', unsafe_allow_html=True)

comparison_df = pd.DataFrame({
    'Model': list(results.keys()),
    'Accuracy': [r['accuracy'] for r in results.values()],
    'Precision': [r['precision'] for r in results.values()],
    'Recall': [r['recall'] for r in results.values()],
    'F1-Score': [r['f1'] for r in results.values()]
})

# Format for display
display_df = comparison_df.copy()
for col in ['Accuracy', 'Precision', 'Recall', 'F1-Score']:
    display_df[col] = display_df[col].apply(lambda x: f"{x:.2%}")

st.dataframe(display_df, use_container_width=True, hide_index=True)

# ============================================================
# COMPARISON CHARTS
# ============================================================
col1, col2 = st.columns(2)

with col1:
    # Accuracy bar chart
    fig = go.Figure(data=[go.Bar(
        x=comparison_df['Model'],
        y=comparison_df['Accuracy'],
        marker_color=[TEAL_DARK, CORAL, TEAL_LIGHT, TEAL_MEDIUM],
        text=[f"{v:.1%}" for v in comparison_df['Accuracy']],
        textposition='outside'
    )])
    fig.update_layout(
        title="Accuracy Comparison",
        plot_bgcolor='white', paper_bgcolor='white',
        height=400, font=dict(color="#2C3E3E"),
        yaxis=dict(range=[0, 0.8], tickformat='.0%')
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    # Grouped metrics
    metrics_long = comparison_df.melt(id_vars='Model', var_name='Metric', value_name='Score')
    fig = px.bar(
        metrics_long, x='Model', y='Score', color='Metric',
        barmode='group',
        color_discrete_sequence=[TEAL_DARK, TEAL_MEDIUM, TEAL_LIGHT, CORAL]
    )
    fig.update_layout(
        title="All Metrics Comparison",
        plot_bgcolor='white', paper_bgcolor='white',
        height=400, font=dict(color="#2C3E3E"),
        yaxis=dict(tickformat='.0%')
    )
    st.plotly_chart(fig, use_container_width=True)

# ============================================================
# CONFUSION MATRICES
# ============================================================
st.markdown('<h3 class="section-header">Confusion Matrices</h3>', unsafe_allow_html=True)

st.markdown("""
<div class="info-box">
    <p style="color:#2C3E3E; margin:0;">
    Each confusion matrix shows the model's classification breakdown. The diagonal represents
    correct predictions; off-diagonal cells represent errors. Replace the placeholder values
    below with your actual confusion matrices from sklearn.
    </p>
</div>
""", unsafe_allow_html=True)

# Sample confusion matrices (placeholders)
classes = ['NO', '>30', '<30']

cms = {
    'Decision Tree':       np.array([[5036, 2393, 826], [2674, 535, 2143], [702, 90, 702]]),
    'k-NN':                np.array([[3302, 3219, 1734], [1873, 2087, 1392], [486, 500, 508]]),
    'SVM':                 np.array([[4623, 1605, 2027], [2675, 1605, 1072], [580, 285, 629]]),
    'Logistic Regression': np.array([[5200, 1485, 1570], [2540, 963, 1849], [466, 386, 642]])
}

selected_model = st.selectbox("Select model:", list(cms.keys()))

col1, col2 = st.columns([2, 1])

with col1:
    cm = cms[selected_model]
    fig = go.Figure(data=go.Heatmap(
        z=cm,
        x=[f"Pred: {c}" for c in classes],
        y=[f"True: {c}" for c in classes],
        colorscale=[[0, '#FFFFFF'], [1, TEAL_DARK]],
        text=cm,
        texttemplate='%{text}',
        textfont={"size": 16, "color": "white"}
    ))
    fig.update_layout(
        title=f"Confusion Matrix — {selected_model}",
        plot_bgcolor='white', paper_bgcolor='white',
        height=450, font=dict(color="#2C3E3E")
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    cm = cms[selected_model]
    correct = np.trace(cm)
    total = cm.sum()
    st.markdown(f"""
    <div class="info-box" style="margin-top:3rem;">
        <h4>Quick Stats</h4>
        <p style="color:#2C3E3E;"><b>Correct:</b> {correct:,} ({correct/total:.1%})</p>
        <p style="color:#2C3E3E;"><b>Incorrect:</b> {total-correct:,} ({(total-correct)/total:.1%})</p>
        <p style="color:#2C3E3E; margin-bottom:0;"><b>Total samples:</b> {total:,}</p>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# WINNER
# ============================================================
st.markdown('<h3 class="section-header">Best Model</h3>', unsafe_allow_html=True)

best_model = comparison_df.loc[comparison_df['Accuracy'].idxmax(), 'Model']
best_acc = comparison_df['Accuracy'].max()

st.markdown(f"""
<div class="info-box" style="border-left: 4px solid #D97757;">
    <h4>🏆 Top Performer: {best_model}</h4>
    <p style="color:#2C3E3E; line-height:1.7;">
    Among the four trained models, <b>{best_model}</b> achieved the highest accuracy of
    <b>{best_acc:.2%}</b>. Its ability to handle non-linear relationships through the RBF kernel
    likely contributed to this advantage. However, it requires more computational resources
    compared to simpler models like Logistic Regression.
    </p>
</div>
""", unsafe_allow_html=True)
