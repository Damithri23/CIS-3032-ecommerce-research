# Predicting E-Commerce Purchase Decisions Using Website Behavior and Pricing Factors

## Project Overview

This project investigates how pricing-related factors influence customer purchase outcomes in e-commerce environments using machine learning techniques.

The study uses the Brazilian E-Commerce Public Dataset (Olist) and applies:

* Logistic Regression for purchase outcome prediction
* K-Means Clustering for customer segmentation
* Streamlit for web application deployment

## Research Objectives

* Analyze the influence of product price and freight value on purchase outcomes.
* Predict customer purchase satisfaction using machine learning.
* Segment customers into meaningful groups based on purchasing characteristics.
* Generate business insights to support data-driven decision making.

## Dataset

Dataset: Brazilian E-Commerce Public Dataset by Olist

Source:
https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

Datasets Used:

* olist_order_items_dataset.csv
* olist_order_reviews_dataset.csv

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Streamlit
* Joblib
* Jupyter Notebook

## Machine Learning Models

### Logistic Regression

Used to predict customer purchase outcomes based on:

* Product Price
* Freight Value

### K-Means Clustering

Used to segment customers based on:

* Price
* Freight Value
* Review Score

## Project Structure

ecommerce-research-project/

├── data/

├── notebooks/

│ ├── ecommerce_logistic_regression.ipynb

│ └── market_segmentation.ipynb

├── app.py

├── model.pkl

└── README.md

## Running the Application

Install dependencies:

pip install pandas numpy scikit-learn matplotlib streamlit joblib

Run Streamlit:

streamlit run app.py

## Results

* Logistic Regression model developed for purchase outcome prediction.
* Customer segmentation performed using K-Means clustering.
* Three customer segments identified:

  * Low Value Customers
  * Regular Customers
  * Premium Customers

## Author

P.S.D.K. Fernando

Faculty of Computing

University of Sri Jayewardenepura

## GitHub Repository

https://github.com/Damithri23/CIS-3032-ecommerce-research.git

