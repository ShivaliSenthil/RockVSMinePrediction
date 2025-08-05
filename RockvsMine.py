import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load("model4.pkl")

# App title and description
st.title("💣 Rock vs Mine Prediction App")
st.markdown(
    """
    Enter the 60 sonar signal features to predict whether the object is a **Rock (R)** or a **Mine (M)**.
    Each feature represents the energy return from a specific sonar frequency band.
    """
)

# Named features for UI
feature_names = [
    "Sonar Frequency Band 1 Energy", "Sonar Frequency Band 2 Energy", "Sonar Frequency Band 3 Energy",
    "Sonar Frequency Band 4 Energy", "Sonar Frequency Band 5 Energy", "Sonar Frequency Band 6 Energy",
    "Sonar Frequency Band 7 Energy", "Sonar Frequency Band 8 Energy", "Sonar Frequency Band 9 Energy",
    "Sonar Frequency Band 10 Energy", "Sonar Frequency Band 11 Energy", "Sonar Frequency Band 12 Energy",
    "Sonar Frequency Band 13 Energy", "Sonar Frequency Band 14 Energy", "Sonar Frequency Band 15 Energy",
    "Sonar Frequency Band 16 Energy", "Sonar Frequency Band 17 Energy", "Sonar Frequency Band 18 Energy",
    "Sonar Frequency Band 19 Energy", "Sonar Frequency Band 20 Energy", "Sonar Frequency Band 21 Energy",
    "Sonar Frequency Band 22 Energy", "Sonar Frequency Band 23 Energy", "Sonar Frequency Band 24 Energy",
    "Sonar Frequency Band 25 Energy", "Sonar Frequency Band 26 Energy", "Sonar Frequency Band 27 Energy",
    "Sonar Frequency Band 28 Energy", "Sonar Frequency Band 29 Energy", "Sonar Frequency Band 30 Energy",
    "Sonar Frequency Band 31 Energy", "Sonar Frequency Band 32 Energy", "Sonar Frequency Band 33 Energy",
    "Sonar Frequency Band 34 Energy", "Sonar Frequency Band 35 Energy", "Sonar Frequency Band 36 Energy",
    "Sonar Frequency Band 37 Energy", "Sonar Frequency Band 38 Energy", "Sonar Frequency Band 39 Energy",
    "Sonar Frequency Band 40 Energy", "Sonar Frequency Band 41 Energy", "Sonar Frequency Band 42 Energy",
    "Sonar Frequency Band 43 Energy", "Sonar Frequency Band 44 Energy", "Sonar Frequency Band 45 Energy",
    "Sonar Frequency Band 46 Energy", "Sonar Frequency Band 47 Energy", "Sonar Frequency Band 48 Energy",
    "Sonar Frequency Band 49 Energy", "Sonar Frequency Band 50 Energy", "Sonar Frequency Band 51 Energy",
    "Sonar Frequency Band 52 Energy", "Sonar Frequency Band 53 Energy", "Sonar Frequency Band 54 Energy",
    "Sonar Frequency Band 55 Energy", "Sonar Frequency Band 56 Energy", "Sonar Frequency Band 57 Energy",
    "Sonar Frequency Band 58 Energy", "Sonar Frequency Band 59 Energy", "Sonar Frequency Band 60 Energy"
]

# Input fields for all 60 features
input_data = []
for feature in feature_names:
    val = st.number_input(f"{feature}", format="%.5f")
    input_data.append(val)

# Predict button
if st.button("Predict"):
    input_array = np.array([input_data])  # Shape: (1, 60)

    # Make prediction
    prediction = model.predict(input_array)[0]

    # Show result
    if prediction == 'R':
        st.success("🪨 Prediction: The object is likely a **Rock**")
    else:
        st.success("💣 Prediction: The object is likely a **Mine**")
