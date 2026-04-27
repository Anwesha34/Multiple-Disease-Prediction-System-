import pickle
import streamlit as st
import suggestions
import chatbot
from streamlit_option_menu import option_menu





# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Multiple Disease Prediction System",
    page_icon="🩺",
    layout="wide"
)

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
.main {
    background-color: #f8fafc;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f172a, #1e293b);
    padding-top: 20px;
}

/* Titles */
.main-title {
    font-size: 38px;
    font-weight: 700;
    color: #111827;
    margin-bottom: 5px;
}

.sub-title {
    font-size: 16px;
    color: #6b7280;
    margin-bottom: 20px;
}

/* Prediction Card */
.prediction-card {
    background: white;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.08);
    margin-bottom: 20px;
    border: 1px solid #e5e7eb;
}

/* Chat Box */
.chat-box {
    background: white;
    border-radius: 18px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.08);
    overflow: hidden;
    border: 1px solid #eee;
    position: sticky;
    top: 20px;
}

.chat-header {
    background: linear-gradient(90deg,#5b5ce2,#7a5cff);
    color: white;
    padding: 16px;
    font-size: 22px;
    font-weight: bold;
}

.chat-sub {
    font-size: 13px;
    font-weight: normal;
}

.user-msg {
    background: #6f63ff;
    color: white;
    padding: 10px 14px;
    border-radius: 14px;
    margin: 8px 0 8px auto;
    width: fit-content;
    max-width: 90%;
}

.bot-msg {
    background: #f3f4f6;
    color: black;
    padding: 10px 14px;
    border-radius: 14px;
    margin: 8px auto 8px 0;
    width: fit-content;
    max-width: 90%;
}
</style>
""", unsafe_allow_html=True)

# ---------- LOAD MODELS ----------
Diabetes_model = pickle.load(
    open("C:/Multiple Disease Prediction System/Models/diabetes_model.pkl", "rb")
)

Diabetes_scaler = pickle.load(
    open("C:/Multiple Disease Prediction System/Models/diabetes_scaler.pkl", "rb")
)

Heart_Disease_model = pickle.load(
    open("C:/Multiple Disease Prediction System/Models/heart_disease_model.pkl", "rb")
)

Heart_scaler = pickle.load(
    open("C:/Multiple Disease Prediction System/Models/heart_scaler.pkl", "rb")
)

# ---------- CHAT HISTORY ----------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        ("bot", "Hello 👋 I'm your AI Health Assistant. How can I help you today?")
    ]

# ---------- SIDEBAR ----------


st.markdown("""
<style>

/* Sidebar background */
section[data-testid="stSidebar"]{
    background: linear-gradient(180deg,#0b1026,#10193d);
}

/* Title style */
.sidebar-title{
    font-size:28px;
    font-weight:800;
    color:#ffffff;
    letter-spacing:1px;
    margin-bottom:2px;
}

/* Subtitle */
.sidebar-subtitle{
    color:#cbd5e1;
    font-size:15px;
    margin-bottom:12px;
}

/* Bottom card */
.sidebar-bottom{
    background:#111827;
    border:1px solid #374151;
    border-radius:16px;
    padding:14px;
    text-align:center;
    color:#e5e7eb;
    margin-top:25px;
}

</style>
""", unsafe_allow_html=True)

with st.sidebar:

    st.markdown("""
    <div class="sidebar-title">🩺 MEDI PREDICT</div>
    <div class="sidebar-subtitle">AI Health Dashboard</div>
    """, unsafe_allow_html=True)

    st.divider()

    selected = option_menu(
        menu_title=None,
        options=[
            "Diabetes Prediction",
            "Heart Disease Prediction",
            "BMI Calculator",
            "Diet Recommendation",
            "About Project"
        ],
        icons=["activity", "heart", "calculator", "apple", "info-circle"],
        default_index=0
    )

    st.markdown("""
    <div class="sidebar-bottom">
        🌿 Stay Healthy,<br>Stay Happy
    </div>
    """, unsafe_allow_html=True)
    
    



# ---------- MAIN LAYOUT ----------
left, right = st.columns([3, 1], gap="medium")

# ==================================================
# LEFT SIDE
# ==================================================
with left:

    st.markdown(
        '<div class="main-title">Multiple Disease Prediction System</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sub-title">AI Based System to Predict Multiple Diseases and Provide Health Assistance</div>',
        unsafe_allow_html=True
    )

    # ---------- DIABETES ----------
    if selected == "Diabetes Prediction":
        st.markdown('<div class="prediction-card">', unsafe_allow_html=True)

        st.title("🩸 Diabetes Prediction Using ML")
        st.write("Enter patient details below:")

        col1, col2, col3 = st.columns(3)

        with col1:
            Pregnancies = st.number_input("Pregnancies", 0, 20, 1)

        with col2:
            Glucose = st.number_input("Glucose Level", 50, 300, 95)

        with col3:
            BloodPressure = st.number_input("Blood Pressure", 40, 250, 70)

        with col1:
            SkinThickness = st.number_input("Skin Thickness", 0, 100, 20)

        with col2:
            Insulin = st.number_input("Insulin Level", 0, 900, 85)

        with col3:
            BMI = st.number_input("BMI", 10.0, 70.0, 24.0)

        with col1:
            DiabetesPedigreeFunction = st.number_input(
                "Diabetes Pedigree Function", 0.0, 3.0, 0.30
            )

        with col2:
            Age = st.number_input("Age", 1, 120, 25)

        if st.button("Predict Diabetes", use_container_width=True):
            user_input = [[
                Pregnancies, Glucose, BloodPressure,
                SkinThickness, Insulin, BMI,
                DiabetesPedigreeFunction, Age
            ]]

            scaled_input = Diabetes_scaler.transform(user_input)
            prediction = Diabetes_model.predict(scaled_input)

            if prediction[0] == 1:
                st.error("The person is Diabetic")
            else:
                st.success("The person is Not Diabetic")

            st.subheader("💡 Health Suggestions")
            diabetes_suggestions = suggestions.get_diabetes_suggestions(prediction[0])

            for item in diabetes_suggestions:
                st.write("•", item)

    # ---------- HEART ----------
    elif selected == "Heart Disease Prediction":
        st.markdown('<div class="prediction-card">', unsafe_allow_html=True)

        st.title("❤️ Heart Disease Prediction Using ML")
        st.write("Enter patient details below:")

        col1, col2, col3 = st.columns(3)

        with col1:
            age = st.number_input("Age", 1, 120, 45)

        with col2:
            sex = st.selectbox(
                "Sex",
                [1, 0],
                format_func=lambda x: "Male" if x == 1 else "Female"
            )

        with col3:
            cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3])

        with col1:
            trestbps = st.number_input("Resting Blood Pressure", 80, 250, 131)

        with col2:
            chol = st.number_input("Cholesterol", 100, 600, 221)

        with col3:
            fbs = st.selectbox("Fasting Blood Sugar >120", [0, 1])

        with col1:
            restecg = st.selectbox("Rest ECG Result", [0, 1, 2])

        with col2:
            thalach = st.number_input("Max Heart Rate", 60, 250, 150)

        with col3:
            exang = st.selectbox("Exercise Angina", [0, 1])

        with col1:
            oldpeak = st.number_input("Oldpeak", 0.0, 10.0, 1.0)

        with col2:
            slope = st.selectbox("Slope", [0, 1, 2])

        with col3:
            ca = st.selectbox("Major Vessels", [0, 1, 2, 3, 4])

        with col1:
            thal = st.selectbox("Thal", [1, 2, 3])

        if st.button("Predict Heart Disease", use_container_width=True):
            user_input = [[
                age, sex, cp, trestbps, chol, fbs,
                restecg, thalach, exang, oldpeak,
                slope, ca, thal
            ]]

            scaled_input = Heart_scaler.transform(user_input)
            prediction = Heart_Disease_model.predict(scaled_input)

            if prediction[0] == 0:
                st.error("The person has Heart Disease")
            else:
                st.success("The person has No Heart Disease")

            st.subheader("💡 Health Suggestions")
            heart_suggestions = suggestions.get_heart_suggestions(prediction[0])

            for item in heart_suggestions:
                st.write("•", item)
                
    

        # ---------- BMI ----------
    elif selected == "BMI Calculator":

        st.markdown('<div class="prediction-card">', unsafe_allow_html=True)

        st.title("⚖️ BMI Calculator")

        height = st.number_input("Height (in meters)", 1.0, 2.5, 1.7)
        weight = st.number_input("Weight (kg)", 30, 200, 70)

        if st.button("Calculate BMI"):
            bmi = weight / (height ** 2)

            st.success(f"Your BMI is {bmi:.2f}")

            if bmi < 18.5:
                st.warning("Underweight")
            elif bmi < 25:
                st.success("Normal")
            elif bmi < 30:
                st.warning("Overweight")
            else:
                st.error("Obese")

        st.markdown('</div>', unsafe_allow_html=True)


    # ---------- DIET ----------
    elif selected == "Diet Recommendation":

        st.markdown('<div class="prediction-card">', unsafe_allow_html=True)

        st.title("🥗 Diet Recommendation")

        condition = st.selectbox(
            "Select Condition",
            ["Normal", "Diabetes", "Heart Disease"]
        )

        if condition == "Diabetes":
            st.write("• Low sugar diet")
            st.write("• High fiber foods")
            st.write("• Avoid processed food")

        elif condition == "Heart Disease":
            st.write("• Low salt diet")
            st.write("• Avoid fried foods")
            st.write("• Eat fruits & vegetables")

        else:
            st.write("• Balanced diet")
            st.write("• Stay hydrated")

        st.markdown('</div>', unsafe_allow_html=True)


    # ---------- ABOUT ----------
    elif selected == "About Project":

        st.markdown('<div class="prediction-card">', unsafe_allow_html=True)

        st.title("📄 About This Project")

        st.write("""
        This is an AI-based Multiple Disease Prediction System.

        🔹 Technologies Used:
        - Machine Learning (Scikit-learn)
        - Streamlit
        - Python

        🔹 Features:
        - Diabetes Prediction
        - Heart Disease Prediction
        - BMI Calculator
        - AI Chatbot
        - Diet Recommendation

        🔹 Purpose:
        To assist users in early disease detection and promote healthy lifestyle.
        """)

        st.markdown('</div>', unsafe_allow_html=True)     
                
                
                
                
                
                

# ==================================================
# RIGHT SIDE CHATBOT
# ==================================================


# ==================================================
# RIGHT SIDE CHATBOT (FIXED SMALL UI)
# ==================================================

with right:

    st.markdown("""
    <div class="chat-box">
        <div class="chat-header">
            🤖 AI Health Assistant
            <div class="chat-sub">Always here to help</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    chat_container = st.container(height=420)

    with chat_container:

        st.markdown("<div class='chat-messages'>", unsafe_allow_html=True)

        for role, msg in st.session_state.chat_history:
            if role == "user":
                st.markdown(
                    f"<div class='user-msg'>{msg}</div>",
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    f"<div class='bot-msg'>{msg}</div>",
                    unsafe_allow_html=True
                )

        st.markdown("</div>", unsafe_allow_html=True)

    question = st.text_input("Type your message...", key="chat_input")

    if st.button("Send", use_container_width=True):
        if question.strip():
            st.session_state.chat_history.append(("user", question))
            answer = chatbot.get_chatbot_response(question)
            st.session_state.chat_history.append(("bot", answer))
            st.rerun()