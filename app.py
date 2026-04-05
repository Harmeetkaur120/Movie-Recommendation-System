import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open('model.pkl', 'rb'))

st.title("🎓 Student Performance Predictor")

st.write("Enter student details:")

studytime = st.slider("Study Time (1-4)", 1, 4, 2)
absences = st.slider("Absences", 0, 100, 5)
G1 = st.slider("Previous Grade G1", 0, 20, 10)
G2 = st.slider("Previous Grade G2", 0, 20, 10)

if st.button("Predict"):
    input_data = np.array([[studytime, absences, G1, G2]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Student is likely to PASS ✅")
    else:
        st.error("Student is likely to FAIL ❌")
