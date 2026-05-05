import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="Healthcare Dashboard", layout="wide")

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

col1.metric("Total Patients", 469)
col2.metric("Male", 281)
col3.metric("Female", 188)
col4.metric("Long-Term PD Rate", "25%")

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
with col1:
    st.subheader("Patients by Condition")
    fig1 = px.pie(
        condition_data,
        values='Count',
        names='Condition',
        hole=0.5
    )
    st.plotly_chart(fig1, use_container_width=True)
    st.info("Parkinson's patients form the largest group.")

# 🔹 Bar Chart
with col2:
    st.subheader("Diagnosis Age by Gender")
    fig2 = px.bar(
        age_data,
        x="Gender",
        y=["Left-handed", "Right-handed"],
        barmode='group'
    )
    st.plotly_chart(fig2, use_container_width=True)
    st.info("Left-handed males show delayed diagnosis.")

# 🔹 Combo Chart
with col3:
    st.subheader("Alcohol Impact by Age")

    fig3 = go.Figure()

    fig3.add_trace(go.Bar(
        x=alcohol_data["Age Group"],
        y=alcohol_data["Patients"],
        name="Patients"
    ))

    fig3.add_trace(go.Scatter(
        x=alcohol_data["Age Group"],
        y=alcohol_data["Worsening %"],
        name="Worsening %",
        yaxis="y2"
    ))

    fig3.update_layout(
        yaxis2=dict(overlaying='y', side='right')
    )

    st.plotly_chart(fig3, use_container_width=True)
    st.info("Mid-age groups show highest worsening.")

st.markdown("---")

# ------------------ SANKEY DIAGRAM ------------------
st.subheader("Patients by Family History")

fig4 = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        label=[
            "PD", "DD", "Patients",
            "No History", "High Risk", "Moderate Risk"
        ]
    ),
    link=dict(
        source=[0, 1, 2, 2, 2],
        target=[2, 2, 3, 4, 5],
        value=[276, 114, 343, 90, 25]
    )
)])

st.plotly_chart(fig4, use_container_width=True)

# ------------------ FOOTER ------------------
st.markdown("---")
st.caption("📌 This dashboard is for analysis purposes only.")