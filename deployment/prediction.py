'''
FINAL PROJECT 
GROUP 003
Members:
    - Faris Arief Mawardi
    - Michael Nathaniel
    - Nadia Nabilla Shafira
    - Noufal Rifata Reyhan

'''

import streamlit as st
import pandas as pd
import pickle

def run():
    st.markdown("<h1 style='text-align: center;'>Model Prediction</h1>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center;'>Please provide imputation data to make predictions with a machine learning model.</h1>", unsafe_allow_html=True)
    st.header('')

    with open('best_rf.pkl', 'rb') as file:
        model = pickle.load(file)

    Store = st.number_input(label='**Insert store ID** *(Whole number only, example: 1, 2, 3, ... )*', min_value=0)

    Temperature = st.number_input(label='**Insert Temperature**',min_value=0.0)

    Fuel_Price = st.number_input(label='**Insert Fuel Price**',min_value=0.0)

    Markdown1 = st.number_input(label='**Insert Markdown 1** *(Whole number only, example: 1, 2, 3, ... )*', min_value=0)

    Markdown2 = st.number_input(label='**Insert Markdown 2** *(Whole number only, example: 1, 2, 3, ... )*', min_value=0)
    
    Markdown3 = st.number_input(label='**Insert Markdown 3** *(Whole number only, example: 1, 2, 3, ... )*', min_value=0)

    Markdown4 = st.number_input(label='**Insert Markdown 4** *(Whole number only, example: 1, 2, 3, ... )*', min_value=0)

    Markdown5 = st.number_input(label='**Insert Markdown 5** *(Whole number only, example: 1, 2, 3, ... )*', min_value=0)

    CPI = st.number_input(label='**Insert CPI**', min_value=0.0)

    Unemployment = st.number_input(label='**Insert Unemployment**', min_value=0.0)
    
    IsHoliday = st.selectbox(label='**Insert Holiday Status**',options=['True', 'False'])

    Type = st.selectbox(label='**Insert Store Type**',options=['A', 'B', 'C'])

    Size = st.number_input(label='**Insert Store Size** *(Whole number only, example: 1, 2, 3, ... )*', min_value=0)

    Dept = st.number_input(label='**Insert Department ID** *(Whole number only, example: 1, 2, 3, ... )*', min_value=0)

    st.write('')
    st.markdown("<h4>Inserted inferece data:</h4>", unsafe_allow_html=True)

    dataInf = pd.DataFrame({
        'Store' : Store,
        'Temperature' : Temperature,
        'Fuel_Price' : Fuel_Price,
        'MarkDown1' : Markdown1,
        'MarkDown2' : Markdown2,
        'MarkDown3' : Markdown3,
        'MarkDown4' : Markdown4,
        'MarkDown5' : Markdown5,
        'CPI' : CPI,
        'Unemployment' : Unemployment,
        'IsHoliday' : IsHoliday,
        'Type' : Type,
        'Size' : Size,
        'Dept' : Dept
    }, index=[0])  

    st.table(dataInf)

    dataInf = dataInf.drop(['Unemployment', 'IsHoliday'], axis = 1)

    if st.button(label='predict'):
    
        # Melakukan prediksi data dummy
        y_pred_inf = model.predict(dataInf)

        st.write('')
        st.markdown("<h4>Prediction Result:</h4>", unsafe_allow_html=True)

        st.write(f'From the outcomes provided, it is evident that the model anticipates sales to be **{y_pred_inf}**.')