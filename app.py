import streamlit as st
import pandas as pd
import requests

st.title("🎓 Student Stress Level Prediction")

# Inputs
anxiety_level = st.slider("Anxiety Level", 0, 21, 11)
self_esteem = st.slider("Self Esteem", 0, 30, 18)
mental_health_history = st.selectbox("Mental Health History", [0, 1])
depression = st.slider("Depression", 0, 27, 12)

headache = st.slider("Headache", 0, 5, 2)
blood_pressure = st.slider("Blood Pressure", 1, 3, 2)
sleep_quality = st.slider("Sleep Quality", 0, 5, 3)
breathing_problem = st.slider("Breathing Problem", 0, 5, 3)

noise_level = st.slider("Noise Level", 0, 5, 3)
living_conditions = st.slider("Living Conditions", 0, 5, 3)
safety = st.slider("Safety", 0, 5, 3)
basic_needs = st.slider("Basic Needs", 0, 5, 3)

academic_performance = st.slider("Academic Performance", 0, 5, 3)
study_load = st.slider("Study Load", 0, 5, 3)
teacher_student_relationship = st.slider(
    "Teacher Student Relationship", 0, 5, 3
)

future_career_concerns = st.slider(
    "Future Career Concerns", 0, 5, 3
)

social_support = st.slider("Social Support", 0, 3, 2)
peer_pressure = st.slider("Peer Pressure", 0, 5, 3)

extracurricular_activities = st.slider(
    "Extracurricular Activities", 0, 5, 3
)

bullying = st.slider("Bullying", 0, 5, 3)

if st.button("Predict Stress Level"):

    data = pd.DataFrame([[
        anxiety_level,
        self_esteem,
        mental_health_history,
        depression,
        headache,
        blood_pressure,
        sleep_quality,
        breathing_problem,
        noise_level,
        living_conditions,
        safety,
        basic_needs,
        academic_performance,
        study_load,
        teacher_student_relationship,
        future_career_concerns,
        social_support,
        peer_pressure,
        extracurricular_activities,
        bullying
    ]], columns=[
        'anxiety_level',
        'self_esteem',
        'mental_health_history',
        'depression',
        'headache',
        'blood_pressure',
        'sleep_quality',
        'breathing_problem',
        'noise_level',
        'living_conditions',
        'safety',
        'basic_needs',
        'academic_performance',
        'study_load',
        'teacher_student_relationship',
        'future_career_concerns',
        'social_support',
        'peer_pressure',
        'extracurricular_activities',
        'bullying'
    ])

    data_dict = data.iloc[0].to_dict()

    response = requests.post(
        "https://student-stress-prediction-3jna.onrender.com/predict",
        json=data_dict
    )

    result = response.json()

    prediction = result["prediction"]
    probabilities = result["probabilities"]

    if prediction == 0:
        st.success("🟢 Low Stress")

    elif prediction == 1:
        st.warning("🟡 Medium Stress")

    else:
        st.error("🔴 High Stress")

    st.subheader("Prediction Probabilities")

    st.write(f"🟢 Low Stress: {probabilities[0]*100:.2f}%")
    st.write(f"🟡 Medium Stress: {probabilities[1]*100:.2f}%")
    st.write(f"🔴 High Stress: {probabilities[2]*100:.2f}%")