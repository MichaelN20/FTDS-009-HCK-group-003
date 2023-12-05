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
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def run():
    st.markdown("<h1 style='text-align: center;'>Exploration Data Analysis</h1>", unsafe_allow_html=True)
    st.write('')
    st.header('')

    # Memanggil data csv
    df = pd.read_csv(r'Walmarts_Inventory_Management_and_Demand_Forecasting.csv')
    
    # menampilakn 10 data teratas
    st.header('Displaying the top 5 data')
    st.table(df.head(5))
    
    # menampilakn 10 data terbawah
    st.header('Displaying the bottom 5 data')
    st.table(df.tail(5))

    st.header('1.')
    image = Image.open('EDA1.png')
    st.image(image, caption='Figure 1: ')
    with st.expander("**Description**"):
        st.write(
            '''
            
            ''')


    st.header('2.')
    image = Image.open('EDA2.png')
    st.image(image, caption='Figure 2: ')
    with st.expander("**Description**"):
        st.write(
            '''
            
            ''')


    st.header('3.')
    image = Image.open('EDA3.png')
    st.image(image, caption='Figure 3: ')
    with st.expander("**Description**"):
        st.write(
            '''
            
            ''')


    st.header('4.')
    image = Image.open('EDA4.png')
    st.image(image, caption='Figure 4: ')
    with st.expander("**Description**"):
        st.write(
            '''
            
            ''')


    st.header('5.')
    list_of_images = ["EDA5.1.png", "EDA5.2.png","EDA5.3.png"]
    for image_path in list_of_images:
        st.image(image_path, caption='Figure 5:', use_column_width=True)
    with st.expander("**Description**"):
        st.write(
            '''
            
            ''')


    st.header('6.')
    image = Image.open('EDA6.png')
    st.image(image, caption='Figure 6: ')
    with st.expander("**Description**"):
        st.write(
            '''
            
            ''')
