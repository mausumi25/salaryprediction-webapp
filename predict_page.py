import streamlit as st
import joblib
import numpy as np

from currency_converter import convert_currency, country_currency

# ------------------------------------
# Load Saved Model
# ------------------------------------
data = joblib.load("model/saved_steps.pkl")

model = data["model"]
country_encoder = data["country_encoder"]
education_encoder = data["education_encoder"]


def show_predict_page():

    st.title("💰 Software Developer Salary Prediction")

    st.write(
        """
        Predict your estimated annual and monthly salary
        based on your country, education, and experience.
        """
    )

    # ------------------------------------
    # User Inputs
    # ------------------------------------

    countries = list(country_encoder.classes_)
    education_levels = list(education_encoder.classes_)

    selected_country = st.selectbox(
        "🌍 Country",
        countries
    )

    selected_education = st.selectbox(
        "🎓 Education Level",
        education_levels
    )

    experience = st.slider(
        "💼 Years of Professional Experience",
        min_value=0,
        max_value=50,
        value=5
    )

    # ------------------------------------
    # Predict Button
    # ------------------------------------

    if st.button("Predict Salary"):

        country = country_encoder.transform([selected_country])[0]
        education = education_encoder.transform([selected_education])[0]

        X = np.array([[country, education, experience]])

        salary = model.predict(X)[0]

        # ------------------------------------
        # Currency Conversion
        # ------------------------------------

        currency = country_currency.get(selected_country, "USD")

        converted_salary = convert_currency(salary, currency)

        symbols = {
            "USD": "$",
            "INR": "₹",
            "EUR": "€",
            "GBP": "£",
            "JPY": "¥",
            "CAD": "C$",
            "AUD": "A$",
            "PKR": "₨",
            "BDT": "৳",
            "NPR": "रू",
            "CNY": "¥",
            "BRL": "R$"
        }

        symbol = symbols.get(currency, "")

        monthly_salary = converted_salary / 12

        # ------------------------------------
        # Display Result
        # ------------------------------------

        st.success("🎉 Prediction Completed Successfully!")

        st.subheader("Prediction Details")

        st.write(f"**🌍 Country:** {selected_country}")
        st.write(f"**🎓 Education:** {selected_education}")
        st.write(f"**💼 Experience:** {experience} Years")

        st.divider()

        st.metric(
            label="💰 Estimated Annual Salary",
            value=f"{symbol}{converted_salary:,.2f}"
        )

        st.metric(
            label="📅 Estimated Monthly Salary",
            value=f"{symbol}{monthly_salary:,.2f}"
        )

        st.caption(f"Currency: {currency}")

        with st.expander("View Salary in USD"):
            st.metric(
                "Estimated Annual Salary (USD)",
                f"${salary:,.2f}"
            )