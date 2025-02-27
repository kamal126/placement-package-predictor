# pip install streamlit
from joblib import load
from numpy import array

import streamlit as st

# load the model

model = load("placement-model.pkl")


st.title("Placement Package Predictor")
st.write("Enter CGPA")

cgpa_input = st.number_input("CGPA",
                             max_value=10.0,
                             min_value=0.0,
                             step=0.1)


if st.button("Predict"): 
    inputf = array([[cgpa_input]])
    prediction = model.predict(inputf)[0]
    st.success(f"Predicted Package: {prediction:.2f}")



# To run the app

# pip install -r requirements.txt
# streamlit run app.py