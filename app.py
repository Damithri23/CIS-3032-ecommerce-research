import joblib
import pandas as pd

# load model
model = joblib.load("model.pkl")

print("E-Commerce Purchase Prediction System")

# user input
price = float(input("Enter product price: "))
freight = float(input("Enter freight value: "))

# create input dataframe
input_data = pd.DataFrame([[price, freight]], columns=['price', 'freight_value'])

# prediction
prediction = model.predict(input_data)

# output result
if prediction[0] == 1:
    print("Prediction: Positive Purchase Outcome")
else:
    print("Prediction: Negative Purchase Outcome")