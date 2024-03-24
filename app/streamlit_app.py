import streamlit as st
import pandas as pd
import requests

# Streamlit app
st.title("Penguin Species Predictor")

# Fetch and display model details
def fetch_model_details(model_id):
    response = requests.get(f"https://render-fastapi-ku5n.onrender.com/model/?model_id={model_id}")
    if response.status_code == 200:
        model_details = response.json()["model"][0]  
        st.write("### Selected Model Details")
        for key, value in model_details.items():
            st.write(f"{key}: {value}")
    else:
        st.error("Failed to fetch model details.")

# Model selection
model_options = {
    "Model 1": 101, 
    "Model 2": 102,
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
    # Preparing the payload for the POST request
    payload = {
        "model_id": model_id - 100,  # Adjusted field name here
        "bill_length_mm": bill_length_mm,
        "bill_depth_mm": bill_depth_mm,
        "flipper_length_mm": flipper_length_mm,
        "body_mass_g": body_mass_g
    }
    # Making the POST request to the FastAPI prediction endpoint
    response = requests.post("https://render-fastapi-ku5n.onrender.com/predict/", json=payload)
    if response.status_code == 200:
        # Processing and displaying the prediction result
        prediction = response.json()["prediction"]
        st.write(f"## Predicted Penguin Species: {prediction}")
    else:
        # Handling failed prediction attempts
        st.error(f"Failed to make prediction. Status code: {response.status_code} Response: {response.text}")
