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

    st.header('Initial Understanding of Weekly Sales Trends')
    image = Image.open('EDA1.png')
    st.image(image, caption='Figure 1: Initial Understanding of Weekly Sales Trends')
    with st.expander("**Description**"):
        st.write(
            '''
            The analysis from the weekly sales line plot reveals several noticeable trends within the available data:

            1. **Maximum Sales Peaks:** There are notable peaks in sales at the end of the year, likely attributed to common Year End Sales promotional strategies. This indicates a significant surge in sales towards the year-end period.

            2. **Price Hike Patterns:** There's a pattern of increased sales coinciding with price hikes at specific times:
                - **Year End (November-December):** This period shows the peak sales, possibly influenced by large-scale promotional campaigns towards the end of the year.
                - **Winter to Spring Transition (February-March):** There's an uptick after the winter months heading into spring, possibly linked to a return in shopping activity after the holiday period.
                - **Summer Season (June-August):** There's an observed increase in sales during the summer months, likely due to holiday activities or summer promotions.

            3. **Drastic Sales Decline:** There's a sharp decline in sales data after October 2012, dropping to zero. This signifies missing data or serious issues in sales records that require further investigation. The loss of data during this period can significantly impact analysis and business planning.

            Further analysis is necessary to better understand sales trends, particularly addressing the data loss after October 2012 and adjusting subsequent business strategies accordingly.
            ''')


    st.header('Data Distribution Analysis')
    image = Image.open('EDA2.png')
    st.image(image, caption='Figure 2: Data Distribution Analysis')
    with st.expander("**Description**"):
        st.write(
            '''
            1. **Store:** Being a categorical variable or unique identifier, it does not have a numerical distribution that can be interpreted through a histogram. This variable merely represents different stores.
            
            2. **Temperature:** The data distribution seems fairly symmetrical with a slightly negative skewness. This indicates a tendency for the data to lean left, meaning the distribution slightly favors lower temperatures. There are no strong indications of extreme tails in the temperature distribution.
            
            3. **Fuel_Price:** The data distribution appears relatively symmetrical with skewness close to zero. The data distribution tends to be normal but may have a slight rightward tail, suggesting a slight tendency for fuel prices to increase.
            
            4. **MarkDown1 - MarkDown5:** These variables have high positive skewness and very high kurtosis, indicating that the data distribution has an extremely long tail to the right. This suggests the presence of very high values (outliers) in these columns.
            
            5. **CPI (Consumer Price Index):** The data distribution seems fairly symmetrical with skewness approaching zero. The data slightly leans towards the right, but it's not too significant.
            
            6. **Unemployment:** The data distribution has slightly positive skewness, indicating a slight tendency to lean towards the right. However, it's not too significant and doesn't show extreme tails in the data distribution.
            
            7. **Size:** The data distribution has negative skewness, indicating a tendency to lean left, but it's not too significant. There are no strong indications of extreme tails in this store size distribution.
            
            8. **Dept:** The data distribution has moderate positive skewness. It leans to the right, indicating a tendency for higher values, but it doesn't show significant extreme tails.
            
            9. **Weekly_Sales:** The data distribution has high positive skewness and very high kurtosis, suggesting an extremely long tail to the right. This indicates the presence of very high values (outliers) in the weekly sales column.

            In conclusion, most variables exhibit asymmetric distributions, with some displaying longer tails on the extreme right (positive). This is crucial to consider in further analysis and statistical or machine learning modeling, especially in handling outliers and adjusting the data distribution to achieve more accurate and representative results.
            ''')


    st.header('Outliers Identification Analysis')
    image = Image.open('EDA3.png')
    st.image(image, caption='Figure 3: Outliers Identification Analysis')
    with st.expander("**Description**"):
        st.write(
            '''
            1. **Store:** No outliers detected.
            
            2. **Temperature:** There's a small amount of data considered outliers at the Lower Bound, around 0.02%, but there are no outliers at the Upper Bound.
            
            3. **Fuel_Price:** No outliers detected.

            4. **MarkDown1-5:** Each MarkDown variable shows outliers, with the highest percentage of outliers in MarkDown3 at approximately 4.50% at the Upper Bound and the lowest in MarkDown1 at around 2.32% at the Upper Bound.
            
            5. **CPI:** No outliers detected.

            6. **Unemployment:** There are around 1.95% of data considered outliers at the Lower Bound and about 5.65% at the Upper Bound.
            
            7. **Size:** No outliers detected.

            8. **Dept:** No outliers detected.

            9. **Weekly_Sales:** Significantly shows outliers with approximately 8.39% of data at the Upper Bound.
                - MarkDown variables (MarkDown1 to MarkDown5), Unemployment, and Weekly_Sales indicate a significant proportion of data considered outliers, both at the upper and lower bounds.
                - There's substantial variation in the presence of outliers among these variables. This highlights the need for handling procedures, such as removal or specific processing, to address these outliers.
            ''')


    st.header('Feature Correlation Analysis')
    image = Image.open('EDA4.png')
    st.image(image, caption='Figure 4: Feature Correlation Analysis')
    with st.expander("**Description**"):
        st.write(
            '''
            From the provided correlation analysis, it is evident that the following features:
            - 'Dept'
            - 'Size'
            - 'Store'
            - 'Date'
            - 'Temperature'
            - 'Fuel_Price'
            - 'MarkDown 1-5'
            - 'Unemployment'
            - 'Type'
            
            Exhibit significant correlations and can be crucial in the process of creating a predictive model for weekly sales estimation. They can serve as vital components in the predictive model creation to estimate weekly sales accurately. Therefore, further exploration is essential to directly observe the influence of these features on the resulting weekly sales.
            ''')


    st.header('Analysis of the Impact of Significant Features on Weekly Sales')
    list_of_images = ["EDA5.1.png", "EDA5.2.png","EDA5.3.png"]
    for image_path in list_of_images:
        st.image(image_path, caption='Figure 5: Analysis of the Impact of Significant Features on Weekly Sales', use_column_width=True)
    with st.expander("**Description**"):
        st.write(
            '''
            Based on the correlation analysis concerning weekly sales ('Weekly Sales'), several significant findings have emerged:

            1. **Department (Dept):** There's a reasonably strong positive correlation (0.52) between department and weekly sales. Higher 'Dept' values tend to relate to higher weekly sales. Department 72 shows the highest sales, indicating that this department might have the most sought-after or top-selling products among others.

            2. **Store Size (Size):** The positive correlation between store size and weekly sales indicates that larger stores have higher weekly sales.

            3. **Store Number (Store):** Though the correlation is not very strong, there is a positive relationship between store number and weekly sales. Some stores show higher weekly sales; for instance, store number 10 stands out with the highest weekly sales among others, suggesting that store number 10 might have an edge contributing to higher sales compared to other stores.

            4. **Date:** The relatively low correlation indicates that the date has an insignificant influence on weekly sales.

            5. **Temperature:** There's a positive correlation between temperature and weekly sales, although not very strong. There seems to be an increase in sales when the temperature ranges between 45-60 Fahrenheit. This phenomenon might indicate certain purchasing preferences associated with environmental temperature. Product placement or promotions tailored to this temperature range could be key to boosting sales.

            6. **Fuel Price:** Despite a weak positive correlation between fuel price and weekly sales, it's evident that sales tend to increase when the fuel price is lower, especially below 3.8. This may indicate that besides consumer sensitivity to cheaper fuel reducing transportation costs, there's also potential for a decrease in product selling prices influenced by deflation. This could increase consumer purchasing power, supporting sales growth during lower fuel price periods.

            7. **Markdown 1-5:** There's moderate or less significant correlation between some types of markdown and weekly sales. For markdown 1, 2, 4, and 5, there's a tendency that lower markdown prices are associated with increased weekly sales. However, for markdown 3, the opposite occurs, where higher markdown values lead to increased weekly sales. This indicates the need for different pricing strategies for each markdown type to achieve optimal sales outcomes.

            8. **Unemployment Rate:** Although there's less significant correlation between the unemployment rate and weekly sales, a tendency was found that weekly sales tend to increase when the unemployment rate ranges between 7.00 to 9.00. This might suggest potential sales growth when the unemployment rate is at those levels. One possible reason could be that within this range, consumers have more income allowing them to make more purchases. Proper marketing strategies are required to capture this opportunity.

            9. **Store Type:** There is a fairly significant correlation between store type and weekly sales, where store type B has the highest average sales, followed by type A and type C with the lowest sales.

            These findings illustrate various factors related to weekly sales and provide insights into their influence on store performance.
            ''')


    st.header('Weekly Sales Analysis')
    image = Image.open('EDA6.png')
    st.image(image, caption='Figure 6: Weekly Sales Analysis')
    with st.expander("**Description**"):
        st.write(
            '''
            Through the depicted line plot of weekly sales, it is noticeable that the weekly sales trend exhibits significant variations. Some noteworthy points observed in this analysis are:

            1. **Spikes in Specific Trends:** Consistent spikes in sales occur during specific periods:
                - **End of Year** (November-December).
                - **Seasonal Transition** from Winter to Spring (February-March).
                - **Summer Months** (June-August).

            2. **Drastic Shifts:** Previously, there was a drastic drop post-October 2012 in the dataset. However, after handling missing values, the trend of sales dropping to zero is no longer visible.

            These patterns indicate sales trends associated with seasonal changes and specific celebrations within a year. This insight is crucial for organizing sales strategies based on identified seasonal patterns, ensuring increased sales and potential profitability.
            ''')
