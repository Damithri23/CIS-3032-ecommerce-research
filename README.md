# Predicting E-Commerce Purchase Decisions Using Website Behavior and Pricing Factors

## Project Overview

This project investigates how pricing-related factors influence customer purchase outcomes in e-commerce environments using machine learning techniques.

The study uses the Brazilian E-Commerce Public Dataset (Olist) and applies:

* Logistic Regression for purchase outcome prediction
* K-Means Clustering for customer segmentation
* Streamlit for web application deployment

---

## Research Objectives

* Analyze the influence of product price and freight value on purchase outcomes.
* Predict customer purchase satisfaction using machine learning.
* Segment customers into meaningful groups based on purchasing characteristics.
* Generate business insights to support data-driven decision making.

---

## Dataset

**Dataset:** Brazilian E-Commerce Public Dataset by Olist  
**Source:** https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce  

### Datasets Used:
* olist_order_items_dataset.csv  
* olist_order_reviews_dataset.csv  

---

## Methodology Summary

The study follows a structured machine learning pipeline:

1. Data preprocessing using Olist dataset  
2. Feature selection (Price, Freight Value, Review Score)  
3. Target variable creation (Positive vs Negative purchase outcome)  
4. Logistic Regression for classification  
5. K-Means clustering for customer segmentation  
6. Model evaluation using accuracy and ROC curve  
7. Visualization of insights using Matplotlib and Seaborn  

---

## Technologies Used

* Python  
* Pandas  
* NumPy  
* Scikit-learn  
* Matplotlib  
* Seaborn  
* Streamlit  
* Joblib  
* Jupyter Notebook  

---

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

---

## Model Evaluation

The Logistic Regression model was evaluated using:

* Accuracy Score  
* Train-test split validation  
* ROC Curve analysis  

These metrics demonstrate moderate but meaningful predictive capability based on pricing features.

---

## Figures and Visualizations

The following figures were generated as part of the analysis:

* Figure 1: Correlation Heatmap of Selected Variables  
* Figure 2: Balanced Dataset Distribution  
* Figure 3: Logistic Regression Feature Coefficients  
* Figure 4: Feature Importance Comparison  
* Figure 5: Elbow Method for Optimal Clusters  
* Figure 6: ROC Curve for Model Evaluation  
* Figure 7: Customer Segments (K-Means Clustering)  
* Figure 8: Average Cluster Characteristics  

All figures are stored in the `figures/` folder.

---

## Project Structure

ecommerce-research-project/

├── data/

├── notebooks/

│   ├── ecommerce_logistic_regression.ipynb

│   ├── market_segmentation.ipynb

├── figures/

├── app.py

├── model.pkl

└── README.md

---

## Running the Application

Install dependencies:

pip install pandas numpy scikit-learn matplotlib seaborn streamlit joblib

Run Streamlit app:

streamlit run app.py

---

## Results Summary

* Logistic Regression model developed for purchase outcome prediction.
* Customer segmentation performed using K-Means clustering.
* Three customer segments identified:
  * Low Value Customers  
  * Regular Customers  
  * Premium Customers  

---

## Outputs

All generated visualizations are stored in the `figures/` folder for reporting and documentation purposes.

---

## Author

P.S.D.K. Fernando  
Faculty of Computing  
University of Sri Jayewardenepura  

---

## GitHub Repository

https://github.com/Damithri23/CIS-3032-ecommerce-research.git