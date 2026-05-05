import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="Healthcare Dashboard", layout="wide")

# ------------------ Load CSS ----------------------
def load_css():
    with open("Style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# ------------------ SIDEBAR ------------------
st.sidebar.title("🧠 Dashboard Menu")

menu = st.sidebar.radio(
    "Navigation",
    ["Demographics", "Disease", "Movement", "Symptoms", "Tremor"]
)

st.sidebar.markdown("---")
st.sidebar.info("Demo Healthcare Dashboard")

# ------------------ MAIN TITLE ------------------
st.title("📊 Demographics Dashboard")

# ------------------ KPI CARDS ------------------
col1, col2, col3, col4 = st.columns(4)

col1.markdown(f'<div class="kpi-card"><h4>Total</h4><h2>{len(df_filtered)}</h2></div>', unsafe_allow_html=True)
col2.markdown(f'<div class="kpi-card"><h4>Male</h4><h2>{(df_filtered["Gender"]=="Male").sum()}</h2></div>', unsafe_allow_html=True)
col3.markdown(f'<div class="kpi-card"><h4>Female</h4><h2>{(df_filtered["Gender"]=="Female").sum()}</h2></div>', unsafe_allow_html=True)
col4.markdown(f'<div class="kpi-card"><h4>Avg Age</h4><h2>{df_filtered["Age"].mean():.1f}</h2></div>', unsafe_allow_html=True)

st.markdown("---")

# ------------------ SAMPLE DATA ------------------
condition_data = pd.DataFrame({
    "Condition": ["PD (Parkinson's)", "DD (Differential)", "HC (Healthy)"],
    "Count": [276, 114, 79]
})

age_data = pd.DataFrame({
    "Gender": ["Male", "Female"],
    "Left-handed": [62.68, 55.08],
    "Right-handed": [55.85, 53.62]
})

alcohol_data = pd.DataFrame({
    "Age Group": ["60-69", "70-79", "50-59", "Under 50", "80+"],
    "Patients": [149, 129, 112, 49, 30],
    "Worsening %": [8, 3, 6, 4, 5]
})

# ------------------ ROW 1 ------------------
col1, col2, col3 = st.columns(3)

# 🔹 Donut Chart
fig = px.pie(df_filtered, names="Condition", hole=0.5)
st.plotly_chart(fig, use_container_width=True)

fig = go.Figure(go.Sankey(
    node=dict(label=["PD","DD","Patients","High Risk"]),
    link=dict(source=[0,1,2], target=[2,2,3], value=[100,80,50])
))
st.plotly_chart(fig)

fig = px.bar(df_filtered, x="Gender", color="Condition")
st.plotly_chart(fig, use_container_width=True)

fig = go.Figure(go.Sankey(
    node=dict(label=["PD","DD","Patients","High Risk"]),
    link=dict(source=[0,1,2], target=[2,2,3], value=[100,80,50])
))
st.plotly_chart(fig)


# ------------------ FOOTER ------------------
st.markdown("---")
st.caption("📌 This dashboard is for analysis purposes only.")
