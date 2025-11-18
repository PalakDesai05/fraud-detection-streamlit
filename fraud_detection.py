import pandas as pd
import numpy as np
import streamlit as st
import joblib
model=joblib.load('fraud_detection_model.pkl')
st.title("Fraud Detection")
st.markdown("Enter the transaction details to predict if it's fraudulent or not.")
st.divider()
transaction_type = st.selectbox("Transaction Type", ['PAYMENT', 'TRANSFER', 'CASH_OUT', 'DEBIT', 'CASH_IN'])
amount = st.number_input("Transaction Amount", min_value=0.0, value=1000.0)
oldbalanceOrg = st.number_input("Old Balance of Origin Account", min_value=0.0, value=10000.0)
newbalanceOrig = st.number_input("New Balance of Origin Account", min_value=0.0, value=9000.0)
oldbalanceDest = st.number_input("Old Balance of Destination Account", min_value=0.0, value=0.0)
newbalanceDest = st.number_input("New Balance of Destination Account", min_value=0.0, value=0.0)

if st.button("Predict"):
    input_data = pd.DataFrame({
        'type': [transaction_type],
        'amount': [amount],
        'oldbalanceOrg': [oldbalanceOrg],
        'newbalanceOrig': [newbalanceOrig],
        'oldbalanceDest': [oldbalanceDest],
        'newbalanceDest': [newbalanceDest]
    })
    prediction = model.predict(input_data)
    
    st.subheader(f"Prediction: '{int(prediction)}'")
    if prediction[0] == 1:
        st.error("The transaction is Fraudulent.")
    else:
        st.success("The transaction is Legitimate.")
        