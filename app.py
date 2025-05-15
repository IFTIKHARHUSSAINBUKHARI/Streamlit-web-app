import streamlit as st
import pandas as pd
import datetime

# Custom CSS for enhanced UI/UX
st.markdown(
    """
    <style>
    body {
        background-color: #0d1117;
        color: #e6edf3;
        font-family: 'Poppins', sans-serif;
    }
    .stApp {
        background-color: #161b22;
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0px 4px 20px rgba(255, 255, 255, 0.1);
    }
    .css-18e3th9 {
        padding: 2rem;
    }
    .stButton>button {
        background: linear-gradient(135deg, #ff8a00, #e52e71);
        color: white;
        border-radius: 12px;
        padding: 12px 24px;
        font-size: 16px;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0px 4px 15px rgba(255, 138, 0, 0.5);
    }
    .stDataFrame {
        background: #21262d;
        border-radius: 12px;
        padding: 15px;
        color: #e6edf3;
    }
    .stMarkdown {
        text-align: center;
        font-size: 18px;
        font-weight: bold;
        color: #ff8a00;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Load or create a workout dataset
if 'workouts' not in st.session_state:
    st.session_state.workouts = pd.DataFrame(columns=["Date", "Exercise", "Duration (mins)", "Calories Burned"])

st.title("🏋️‍♂️ Fitness Tracker App")
st.write("Track your workouts and visualize your progress with an enhanced experience.")

# User input for workout logging
date = st.date_input("📅 Select Date", datetime.date.today())
exercise = st.selectbox("🏋️ Select Exercise", ["Running", "Cycling", "Swimming", "Weight Training", "Yoga", "HIIT"])
duration = st.number_input("⏳ Duration (mins)", min_value=1, max_value=300, step=1)
calories = st.number_input("🔥 Calories Burned", min_value=1, max_value=2000, step=1)

if st.button("✅ Add Workout"):
    new_data = pd.DataFrame({
        "Date": [date],
        "Exercise": [exercise],
        "Duration (mins)": [duration],
        "Calories Burned": [calories]
    })
    st.session_state.workouts = pd.concat([st.session_state.workouts, new_data], ignore_index=True)
    st.success("🎉 Workout added successfully!")

# Display logged workouts
st.subheader("📋 Workout Log")
st.dataframe(st.session_state.workouts)

# Visualization
st.subheader("📈 Workout Progress")
if not st.session_state.workouts.empty:
    st.session_state.workouts["Date"] = pd.to_datetime(st.session_state.workouts["Date"])
    fig = px.line(st.session_state.workouts, x="Date", y="Calories Burned", color="Exercise", title="🔥 Calories Burned Over Time", template="plotly_dark")
    st.plotly_chart(fig)
else:
    st.write("No workout data available yet. Start logging your workouts!")

# Footer
st.markdown("---")
st.markdown("### 🚀 Made by Iftikhar")
