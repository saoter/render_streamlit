import streamlit as st
import pandas as pd
from joblib import load

# Function to load a model
def load_model(model_name):
    return load(model_name)

# Load models
models = {
    "Model 1": load_model("models/model_v1.joblib"),
    "Model 2": load_model("models/model_v2.joblib"),
}

# Streamlit app
st.title("Penguin Species Predictor")

# Model selection
model_name = st.selectbox("Select a Model", options=list(models.keys()))
model = models[model_name]

# User inputs for features
st.write("## Enter Penguin Features")

bill_length_mm = st.number_input("Bill Length (mm)", min_value=0.0, format="%.2f")
bill_depth_mm = st.number_input("Bill Depth (mm)", min_value=0.0, format="%.2f")
flipper_length_mm = st.number_input("Flipper Length (mm)", min_value=0.0, format="%.2f")
body_mass_g = st.number_input("Body Mass (g)", min_value=0.0, format="%.2f")

# Predict button
if st.button("Predict"):
    # Create a DataFrame with the input features
    input_data = pd.DataFrame(
        [[bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g]],
        columns=["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]
    )
    
    # Make prediction
    prediction = model.predict(input_data)
    
    # Display prediction
    st.write(f"## Predicted Penguin Species: {prediction[0]}")
