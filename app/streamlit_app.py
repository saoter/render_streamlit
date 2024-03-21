import streamlit as st
import pandas as pd
from joblib import load

# Streamlit app
st.title("Penguin Species Predictor")

# Fetch and display model details
def fetch_model_details(model_id):
    response = requests.get(f"https://render-fastapi-ku5n.onrender.com/model/?model_id={model_id}")
    if response.status_code == 200:
        model_details = response.json()["model"][0]  # Assuming the response has a "model" key with a list of models
        st.write("### Selected Model Details")
        for key, value in model_details.items():
            st.write(f"{key}: {value}")
    else:
        st.error("Failed to fetch model details.")

# Model selection
model_options = {
    "Model 1": 1,  # Assuming model IDs are integers
    "Model 2": 2,
}
model_name = st.selectbox("Select a Model", options=list(model_options.keys()))
model_id = model_options[model_name]

# Display model details for the selected model
fetch_model_details(model_id)

# User inputs for features
st.write("## Enter Penguin Features")
bill_length_mm = st.number_input("Bill Length (mm)", min_value=0.0, format="%.2f")
bill_depth_mm = st.number_input("Bill Depth (mm)", min_value=0.0, format="%.2f")
flipper_length_mm = st.number_input("Flipper Length (mm)", min_value=0.0, format="%.2f")
body_mass_g = st.number_input("Body Mass (g)", min_value=0.0, format="%.2f")

# Predict button
if st.button("Predict"):
    # API payload
    payload = {
        "prediction_model_id": model_id,
        "bill_length_mm": bill_length_mm,
        "bill_depth_mm": bill_depth_mm,
        "flipper_length_mm": flipper_length_mm,
        "body_mass_g": body_mass_g
    }
    # Make API call for prediction
    response = requests.post("https://render-fastapi-ku5n.onrender.com/predict/", json=payload)
    if response.status_code == 200:
        prediction = response.json()["prediction"]
        # Display prediction
        st.write(f"## Predicted Penguin Species: {prediction}")
    else:
        st.error("Failed to make prediction.")
