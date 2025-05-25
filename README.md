# Predicting Individual Healthcare Costs


## 1. Introduction

Healthcare costs vary significantly based on individual attributes such as age, BMI, smoking status, and geographic region. These costs are a major consideration for both individuals and insurance companies. Accurately estimating them can inform pricing strategies, promote preventive care, and support financial planning.

This project leverages a real-world dataset containing demographic and lifestyle features of insured individuals to develop a predictive model. The goal is to estimate medical charges and uncover the primary cost drivers, with a deployable solution that offers direct user interaction.



## 2. Objective

- **Primary Goal:**  
  Develop a machine learning model to **predict healthcare charges** using demographic and lifestyle inputs.

- **Secondary Goals:**  
  - Determine the most significant factors influencing medical expenses.  
  - Offer actionable insights to help users reduce potential costs.  
  - Build and deploy an interactive **Flask web application** on **Microsoft Azure**.



## 3. Expected Results

- A trained regression model for healthcare cost prediction.  
- Interpretability analysis using SHAP to explain model outputs.  
- Data visualizations including:  
  - Actual vs. predicted cost comparisons.   
- A user-friendly **Flask web application** that:  
  - Accepts user input for features (age, BMI, smoker, etc.).  
  - Returns predicted healthcare costs.  
- Deployed application on **Azure App Service**, accessible via a public URL.



## 4. Azure Deployment Plan (with Flask)

- **Model Development:**  
  - Train model.  
  - Save the model using `pickle`.

- **Web Application (Flask):**  
  - Build a Flask app with forms to collect user input.  
  - Load the trained model and return predictions in the response view.
