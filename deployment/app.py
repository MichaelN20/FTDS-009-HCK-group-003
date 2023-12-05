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
from PIL import Image
import eda
import prediction


st.sidebar.title("Menu")
page = st.sidebar.selectbox(label='Select Page', options=['Home Page', 'Exploration Data Analysis', 'Prediction'])

if page == 'Home Page':
    st.markdown("<h1 style='text-align: center;'>Walmart's Inventory Management and Demand Forecasting</h1>", unsafe_allow_html=True)
    
    img = Image.open('walmart.jpg')
    st.image(img)
    st.caption("Source: https://www.retailtouchpoints.com/wp-content/uploads/2020/09/Walmart-Redesign-exterior-960x540.jpg")

    st.write(
    """
    <div style='text-align: center; font-weight: bold; font-size: 1.2em;'>FINAL PROJECT</div>
    """,
    unsafe_allow_html=True)
    st.write('**Name      :**'
             f"""
        <div style="font-size: 15px; text-align: justify;">
        <ul> 
            <li>**Faris Arief Mawardi** as Data Analyist</li>
            <li>**Michael Nathaniel** as Data Engineer</li>
            <li>**Nadia Nabilla Shafira** as Data Scientist</li>
            <li>**Noufal Rifata Reyhan** as Data Scientist</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True)        
    st.write("**About Dataset   :** "
        f"""
        <div style="font-size: 15px; text-align: justify;">
        <ul> 
            <li>This dataset comprises sales records from multiple stores, encompassing various parameters such as store ID, date of sales, temperature, fuel prices, promotional markdown details (MarkDown1 to MarkDown5), consumer price index (CPI), unemployment rate, holiday occurrences, store type, size, department number, and the recorded weekly sales. The data includes comprehensive information about sales, store specifics, economic indicators, and promotional activities, providing an overview of retail transactions and contextual factors impacting sales across different stores within a certain timeframe.</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True)

    with st.expander("Background"):
        st.caption("Walmart, one of the world's largest retailers, operates in a variety of locations with different types and sizes of stores. Knowledge of sales trends and the factors that influence them can help Walmart optimize inventory, prevent overstocking or understocking, and improve operational efficiency and customer satisfaction. Inventory management is a crucial aspect of retail operations, as experienced by Walmart. Efficient inventory management requires a deep understanding of the factors that influence sales and the use of accurate forecasting models.")

    with st.expander("Problem Statement"):
        st.caption(
    f"""
    <div style="font-size: 15px; text-align: justify;">
    <ul> 
        <li>Who: This project was carried out to provide insight into the Walmart Management Team responsible for supply chain and sales.</li>
        <li>What: The main problem behind this project is the lack of accurate forecasting of sales in various Walmart stores, resulting in difficulties in managing inventory efficiently.</li>
        <li>Where: Across Walmart stores operating in various locations and having various store types.</li>
        <li>Why: The inability to forecast sales accurately can result in excessive stock or out-of-stock, which impacts product availability and results in financial losses.</li>
        <li>How: By implementing the right forecasting model and utilizing it to optimize inventory management strategies, Walmart can improve operational efficiency and increase customer satisfaction</li>
    </ul>
    </div>
    Built an accurate sales forecasting model for various Walmart stores by leveraging factors such as date, store type, promotions, and environmental information. In addition, the results of the forecasting model will be used to optimize inventory levels to prevent excess or shortage of stock which could disrupt product availability and increase store operational efficiency and customer satisfaction.
    """,
    unsafe_allow_html=True)
        
    with st.expander("Conclusion of Problem Statement"):
        st.caption('The lack of accuracy in sales forecasting at Walmart stores results in difficulties in efficient inventory management and can impact potential financial losses. One improvement step that can be taken as a solution is the application of appropriate forecasting models to increase operational efficiency and customer satisfaction.')

    st.write('**Work Flow     :**')
    img = Image.open('miro.png')
    st.image(img)



elif page == 'Exploration Data Analysis':
    eda.run()
else:
    prediction.run()