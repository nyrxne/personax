import streamlit as st
from core.models import UserProfile
from core.calculators import HealthCalculator
from core.profile_engine import ProfileEngine
from core.recommendations import RecommendationEngine
from core.personality import PersonalityEngine
from core.scoring import ScoreEngine
from ui.dashboard import render_dashboard
from exports.pdf_exports import generate_pdf

st.set_page_config(
    page_title="PersonaX AI",
    page_icon="🧠",
    layout="wide"
)

st.title("PersonaX AI")
st.caption("Personal Intelligence Dashboard")

with st.sidebar:
    st.header("Profile Builder")
    name = st.text_input("Name")
    age = st.number_input("Age", 1, 120)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    height = st.number_input("Height (cm)", 50, 250)
    weight = st.number_input("Weight (kg)", 20, 300)
    occupation = st.text_input("Occupation")
    education = st.selectbox("Education", [
        "High School", "Diploma", "Bachelor's",
        "Master's", "PhD"
    ])

    skills = st.text_input("Skills (comma separated)")
    hobbies = st.text_input("Hobbies (comma separated)")
    fav_lang = st.selectbox(
        "Favorite Programming Language",
        ["Python", "JavaScript", "C++", "Java", "Go", "Rust"]
    )

    career_goals = st.text_area("Career Goals")
    generate_clicked = st.button("Generate Persona")

if generate_clicked:
    profile = UserProfile(
        name=name,
        age=age,
        gender=gender,
        height=height,
        weight=weight,
        occupation=occupation,
        education=education,
        skills=[x.strip() for x in skills.split(",") if x],
        hobbies=[x.strip() for x in hobbies.split(",") if x],
        favorite_language=fav_lang,
        career_goals=career_goals
    )

    st.session_state.profile = profile
    st.session_state.health = HealthCalculator(profile)
    st.session_state.personality = PersonalityEngine(profile)
    st.session_state.recommendations = RecommendationEngine(profile)
    st.session_state.score = ScoreEngine(profile)

    st.session_state.profile_data = ProfileEngine(
        st.session_state.profile,
        st.session_state.health,
        st.session_state.personality,
        st.session_state.recommendations
    ).generate()

    st.session_state.pdf_path = generate_pdf(st.session_state.profile, st.session_state.profile_data)
    st.session_state.generated = True

if st.session_state.get("generated", False):
    render_dashboard(
        st.session_state.profile,
        st.session_state.health,
        st.session_state.personality,
        st.session_state.recommendations,
        st.session_state.score,
        st.session_state.profile_data
    )

    with open(st.session_state.pdf_path, "rb") as file:
        st.download_button(
            label="Download PDF Report",
            data=file,
            file_name="persona_report.pdf",
            mime="application/pdf"
        )
