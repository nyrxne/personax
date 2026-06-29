import streamlit as st
import plotly.express as px
import pandas as pd

def render_dashboard(
    profile,
    health,
    personality,
    recommendations,
    score,
    profile_data
):
    st.subheader("Profile Summary")

    col1, col2, col3 = st.columns(3)

    col1.metric("BMI", health.bmi())
    col2.metric("Water (L)", health.water_requirement())
    col3.metric("Profile Score", score.calculate())

    st.progress(score.calculate())

    st.subheader("Personality Radar")

    traits = personality.analyze()

    df = pd.DataFrame({
        "Trait": list(traits.keys()),
        "Score": list(traits.values())
    })

    fig = px.line_polar(
        df,
        r="Score",
        theta="Trait",
        line_close=True
    )

    st.plotly_chart(fig)

    st.subheader("Career Suggestions")
    st.write(recommendations.career_suggestions())

    st.subheader("Learning Roadmap")
    st.write(recommendations.roadmap())

    st.subheader("AI Profile")
    st.json(profile_data)