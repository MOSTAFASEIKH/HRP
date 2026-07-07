import streamlit as st
import joblib

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="House Rent Prediction",
    page_icon="🏠",
    layout="centered"
)

# --------------------------------------------------
# Load Trained Model
# --------------------------------------------------
model = joblib.load("models/house_rent_prediction_model.pkl")

# --------------------------------------------------
# Application Title
# --------------------------------------------------
st.title("🏠 House Rent Prediction")
st.markdown("### Predict the monthly rent of a house using Machine Learning.")

st.write("---")

st.success("Model loaded successfully!")
# --------------------------------------------------
# Categorical Inputs
# --------------------------------------------------

area_type = st.selectbox(
    "Area Type",
    ["Carpet Area", "Super Area", "Built Area"]
)

city = st.selectbox(
    "City",
    ["Bangalore", "Chennai", "Delhi", "Hyderabad", "Kolkata", "Mumbai"]
)

furnishing = st.selectbox(
    "Furnishing Status",
    ["Furnished", "Semi-Furnished", "Unfurnished"]
)

tenant = st.selectbox(
    "Tenant Preferred",
    ["Bachelors", "Bachelors/Family", "Family"]
)

contact = st.selectbox(
    "Point of Contact",
    ["Contact Agent", "Contact Builder", "Contact Owner"]
)

locality = st.selectbox(
    "Area Locality",
    sorted(locality_mapping.keys())
)
