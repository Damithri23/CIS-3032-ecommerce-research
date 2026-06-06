import streamlit as st
import joblib
import os

# Load model
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
model = joblib.load(model_path)

st.title("E-Commerce Purchase Prediction System")
st.write("Predict whether a customer will complete a purchase based on price and freight value")

# Input fields
price = st.number_input("Enter Product Price", min_value=0.0)
freight = st.number_input("Enter Freight Value", min_value=0.0)

# Prediction button
if st.button("Predict"):
    input_data = [[price, freight]]
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Positive Purchase Outcome (Customer likely to buy)")
    else:
        st.error("Negative Purchase Outcome (Customer less likely to buy)")
        