import streamlit as st
import numpy as np
import joblib

# Load saved model and scaler
model = joblib.load('loan_model.pkl')
scaler = joblib.load('scaler.pkl')

st.title("🏦 Loan Eligibility Predictor")

# Input fields
Gender = st.selectbox("Gender", ['Male', 'Female'])
Married = st.selectbox("Married", ['Yes', 'No'])
Dependents = st.selectbox("Dependents", ['0', '1', '2', '3+'])
Education = st.selectbox("Education", ['Graduate', 'Not Graduate'])
Self_Employed = st.selectbox("Self Employed", ['Yes', 'No'])
ApplicantIncome = st.number_input("Applicant Income", min_value=0)
CoapplicantIncome = st.number_input("Coapplicant Income", min_value=0)
LoanAmount = st.number_input("Loan Amount (in 1000s)", min_value=0)
Loan_Amount_Term = st.number_input("Loan Term (in days)", min_value=0)
Credit_History = st.selectbox("Credit History", ['1.0', '0.0'])
Property_Area = st.selectbox("Property Area", ['Urban', 'Semiurban', 'Rural'])

# Encoding inputs
Education_Not_Graduate = 1 if Education == 'Not Graduate' else 0
Property_Area_Semiurban = 1 if Property_Area == 'Semiurban' else 0
Property_Area_Urban = 1 if Property_Area == 'Urban' else 0
Dependents_1 = 1 if Dependents == '1' else 0
Dependents_2 = 1 if Dependents == '2' else 0
Dependents_3_plus = 1 if Dependents == '3+' else 0

Gender = 1 if Gender == 'Male' else 0
Married = 1 if Married == 'Yes' else 0
Self_Employed = 1 if Self_Employed == 'Yes' else 0
Credit_History = float(Credit_History)

# Final input
input_data = [[
    Gender, Married, Self_Employed, ApplicantIncome, CoapplicantIncome,
    LoanAmount, Loan_Amount_Term, Credit_History,
    Education_Not_Graduate, Dependents_1, Dependents_2, Dependents_3_plus,
    Property_Area_Semiurban, Property_Area_Urban
]]

# Predict
if st.button("Check Loan Eligibility"):
    
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.success("✅ Eligible for Loan!")
    else:
        st.error("❌ Not Eligible for Loan.")
