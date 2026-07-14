import streamlit as st
import pandas as pd
import plotly.express as px


def show_explore_page():

    st.title("📊 Explore Stack Overflow Survey")

    df = pd.read_csv("data/survey_results_public.csv")

    st.subheader("Dataset Shape")
    st.write(df.shape)

    st.subheader("First Five Rows")
    st.dataframe(df.head())

    st.subheader("Top 10 Countries")

    country_count = df["Country"].value_counts().head(10)

    fig = px.bar(
        x=country_count.index,
        y=country_count.values,
        labels={
            "x": "Country",
            "y": "Number of Developers"
        },
        title="Top 10 Countries"
    )

    st.plotly_chart(fig)

    st.subheader("Education Level")

    education = df["EdLevel"].value_counts()

    fig = px.pie(
        values=education.values,
        names=education.index,
        title="Education Distribution"
    )

    st.plotly_chart(fig)

    salary = df["ConvertedComp"].dropna()

    fig = px.histogram(
        salary,
        nbins=50,
        title="Salary Distribution"
    )

    st.plotly_chart(fig)

    experience = df["YearsCodePro"].dropna()

    fig = px.histogram(
        experience,
        title="Years of Professional Coding Experience"
    )

    st.plotly_chart(fig)