import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open('model.pkl', 'rb'))

st.title("🎓 Student Performance Predictor")

hours = st.slider("Study Hours", 0, 10, 1)
attendance = st.slider("Attendance (%)", 0, 100, 50)

if st.button("Predict"):
    input_data = np.array([[hours, attendance]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Student is likely to PASS ✅")
    else:
        st.error("Student is likely to FAIL ❌")
