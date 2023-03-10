# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 03:47:09 2023

@author: RBB
"""


import numpy as np
import pickle
import pandas as pd

import streamlit as st 

from PIL import Image

pickle_in = open("C:/Users/Admin/Desktop/project/RF_model.pkl","rb")
loaded_model=pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def Churn_prediction(voice_plan, voice_messages, intl_plan, intl_mins, intl_calls, intl_charge, day_mins, day_calls, day_charge, eve_mins, eve_calls, eve_charge, night_mins, night_calls, night_charge, customer_calls):
    
    prediction=loaded_model.predict([[voice_plan, voice_messages, intl_plan, intl_mins, intl_calls, intl_charge, day_mins, day_calls, day_charge, eve_mins, eve_calls, eve_charge, night_mins, night_calls, night_charge, customer_calls]])
    print(prediction)
    if (prediction[0] == 0):
        return 'The person will not be churned'
    else:
        return 'The person will be churned'
    



def main():
    
    st.title('Churn prediction Web App')
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Churn Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    
    voice_plan = st.sidebar.selectbox('Voiceplan',('1','0'))
    voice_messages = st.sidebar.number_input(' voice_message')
    intl_plan = st.sidebar.selectbox('Intlplan',('1','0'))
    intl_mins = st.sidebar.number_input(' intl mins')
    intl_calls = st.sidebar.number_input('intl calls')
    intl_charge = st.sidebar.number_input('intl charge')
    day_mins = st.sidebar.number_input('day mins')
    day_calls = st.sidebar.number_input('day calls')
    day_charge = st.sidebar.number_input('day charge')
    eve_mins = st.sidebar.number_input('eve mins')
    eve_calls = st.sidebar.number_input('eve calls')
    eve_charge = st.sidebar.number_input('eve charge')
    night_mins = st.sidebar.number_input('night mins')
    night_calls = st.sidebar.number_input('night calls')
    night_charge = st.sidebar.number_input('night charge')
    customer_calls = st.sidebar.number_input('no of customer_calls')
    
    #code for prediction (the result of prediction will return in this empty string)
    Churn = ''
    
    #creating button for prediction
    if st.button('Churn Result'):
        Churn = Churn_prediction(voice_plan, voice_messages, intl_plan, intl_mins, intl_calls, intl_charge, day_mins, day_calls, day_charge, eve_mins, eve_calls, eve_charge, night_mins, night_calls, night_charge, customer_calls)
    
    
    st.success(Churn)
    
    
    
if __name__ == '__main__':
    main()
    
    
    