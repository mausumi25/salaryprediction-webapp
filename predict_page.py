import streamlit as st
import joblib
import numpy as np

# -----------------------------
# Load Saved Model
# -----------------------------
data = joblib.load("model/saved_steps.pkl")

model = data["model"]
country_encoder = data["country_encoder"]
education_encoder = data["education_encoder"]


# -----------------------------
# Prediction Page
# -----------------------------
def show_predict_page():

    st.title("💰 Software Developer Salary Prediction")

    st.write(
        """
        ### Fill in the details below to predict your estimated annual salary.
        """
    )

    # -----------------------------
    # User Inputs
    # -----------------------------
    countries = list(country_encoder.classes_)
    education_levels = list(education_encoder.classes_)

    country = st.selectbox(
        "🌍 Country",
        countries
    )

    education = st.selectbox(
        "🎓 Education Level",
        education_levels
    )

    experience = st.slider(
        "💼 Years of Professional Coding Experience",
        min_value=0,
        max_value=50,
        value=5
    )

    # -----------------------------
    # Prediction Button
    # -----------------------------
    if st.button("Predict Salary"):

        country = country_encoder.transform([country])[0]
        education = education_encoder.transform([education])[0]

        X = np.array([[country, education, experience]])

        salary = model.predict(X)

        st.success("Prediction Completed ✅")

        st.metric(
            label="Estimated Annual Salary",
            value=f"${salary[0]:,.2f}"
        )