# 🎓 Student Performance Predictor (Machine Learning + Streamlit)

## 📌 Overview

This project is a **supervised machine learning application** that predicts whether a student will pass or fail based on academic performance and study-related factors.

The model is trained using a real-world dataset and deployed as an interactive web application using Streamlit.

---

## 🚀 Features

* Predicts student performance (Pass/Fail)
* Uses real-world dataset for training
* Interactive and user-friendly web interface
* Real-time predictions based on user input

---

## 🧠 Machine Learning Approach

* Algorithm: Logistic Regression
* Type: Supervised Learning (Binary Classification)
* Target Variable: Pass (1) / Fail (0)

### 📊 Input Features:

* Study Time
* Absences
* First Period Grade (G1)
* Second Period Grade (G2)

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit

---

## 📂 Dataset

* Dataset: Student Performance Dataset
* Source: Kaggle
* Description: Contains student-related attributes such as study time, absences, and grades

---

## ⚙️ Project Structure

```
project/
│── app.py          # Streamlit application
│── model.py        # Model training script
│── model.pkl       # Trained model file
│── student-mat.csv # Dataset
│── README.md       # Documentation
```

---

## ▶️ How to Run the Project

### 1. Install Dependencies

```
pip install streamlit scikit-learn pandas numpy
```

### 2. Train the Model

```
python model.py
```

### 3. Run the Application

```
streamlit run app.py
```

---

## 🎯 Usage

1. Enter student details such as study time, absences, and previous grades
2. Click the **Predict** button
3. View whether the student is likely to pass or fail

---

## 📊 Model Evaluation

* The model is evaluated using accuracy score
* Provides a measure of how well the model predicts outcomes on test data

---

## 🔮 Future Improvements

* Use larger and more diverse datasets
* Add more features (e.g., extracurricular activities, sleep patterns)
* Improve UI/UX design
* Deploy application on cloud platforms

---

## 🤝 Contribution

Contributions are welcome. Feel free to fork the repository and improve the project.

---

## 📬 Contact

Harmeet Kaur
GitHub: https://github.com/Harmeetkaur120
LinkedIn: https://linkedin.com

---

## ⭐ Acknowledgment

This project was developed to understand the fundamentals of Machine Learning and model deployment using Streamlit.
