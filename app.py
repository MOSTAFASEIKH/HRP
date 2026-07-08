import streamlit as st
import pandas as pd
import joblib


# ---------------------------------------
# Page Configuration
# ---------------------------------------

st.set_page_config(
    page_title="House Rent Prediction",
    page_icon="🏠",
    layout="wide"
)


# ---------------------------------------
# Load Model
# ---------------------------------------

pipeline = joblib.load("models/house_rent_pipeline.pkl")
localities = joblib.load("models/localities.pkl")


# ---------------------------------------
# Header
# ---------------------------------------

st.title("🏠 House Rent Prediction")

st.markdown(
"""
### Predict monthly house rent using Machine Learning

This application uses a **Gradient Boosting Regression model**
trained on real house rental data.
"""
)

st.divider()


# ---------------------------------------
# Sidebar
# ---------------------------------------

st.sidebar.header("🏠 About Model")

st.sidebar.info(
"""
**Algorithm**

Gradient Boosting Regressor


**Dataset**

House Rent Dataset


**Framework**

Scikit-learn + Streamlit
"""
)


# ---------------------------------------
# Input Section
# ---------------------------------------

st.subheader("🏡 Property Details")


col1, col2 = st.columns(2)


with col1:

    bhk = st.number_input(
        "BHK",
        min_value=1,
        max_value=10,
        value=2
    )


    size = st.number_input(
        "Size (sq.ft)",
        min_value=100,
        max_value=10000,
        value=1000,
        step=50
    )


    bathroom = st.number_input(
        "Bathrooms",
        min_value=1,
        max_value=10,
        value=2
    )


    current_floor = st.number_input(
        "Current Floor",
        min_value=-2,
        max_value=100,
        value=1
    )


    total_floors = st.number_input(
        "Total Floors",
        min_value=1,
        max_value=100,
        value=5
    )


with col2:


    area_type = st.selectbox(
        "Area Type",
        [
            "Super Area",
            "Carpet Area",
            "Built Area"
        ]
    )


    city = st.selectbox(
        "City",
        [
            "Bangalore",
            "Chennai",
            "Delhi",
            "Hyderabad",
            "Kolkata",
            "Mumbai"
        ]
    )


    locality = st.selectbox(
        "Area Locality",
        localities
    )


    furnishing = st.selectbox(
        "Furnishing Status",
        [
            "Furnished",
            "Semi-Furnished",
            "Unfurnished"
        ]
    )


    tenant = st.selectbox(
        "Tenant Preferred",
        [
            "Bachelors",
            "Bachelors/Family",
            "Family"
        ]
    )


    contact = st.selectbox(
        "Point of Contact",
        [
            "Contact Agent",
            "Contact Builder",
            "Contact Owner"
        ]
    )


st.divider()


# ---------------------------------------
# Prediction
# ---------------------------------------


if st.button(
    "🔍 Predict Rent",
    use_container_width=True
):

    input_df = pd.DataFrame({

        "BHK":[bhk],
        "Size":[size],
        "Area Type":[area_type],
        "Area Locality":[locality],
        "City":[city],
        "Furnishing Status":[furnishing],
        "Tenant Preferred":[tenant],
        "Bathroom":[bathroom],
        "Point of Contact":[contact],

        # Default posting date features
        "Year":[2022],
        "Month":[5],
        "Day":[18],

        "Current Floor":[current_floor],
        "Total Floors":[total_floors]

    })


    prediction = pipeline.predict(input_df)


    st.success("Prediction Completed")


    st.metric(
        label="🏠 Predicted Monthly Rent",
        value=f"₹ {prediction[0]:,.0f}"
    )


# ---------------------------------------
# Footer
# ---------------------------------------

st.divider()


st.caption(
"""
Developed by MOSTAFA Sk |
House Rent Prediction using Machine Learning
"""
)


with st.expander("ℹ About this Project"):

    st.write(
    """
    ✔ End-to-end ML pipeline

    ✔ Automated preprocessing

    ✔ Gradient Boosting Regression

    ✔ Streamlit deployment
    """
    )