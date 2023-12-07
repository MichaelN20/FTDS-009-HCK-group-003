# **Walmart's Inventory Management and Demand Forecasting**

### **URL:**

[Deployment](https://huggingface.co/spaces/michaeln20/FTDS-009-HCK-group-003) | [Data Exploration Dashboard](https://public.tableau.com/app/profile/faris.arief.mawardi/viz/WalmartsInventoryManagementandDemandForecasting/Dashboard1?publish=yes) | [Features Correlation Analysis Dashboard](https://public.tableau.com/app/profile/faris.arief.mawardi/viz/CorrelationAnalysisofWalmartsInventoryManagementandDemandForecasting/Dashboard2?publish=yes) | [Insights of Data Exploration](https://public.tableau.com/app/profile/faris.arief.mawardi/viz/InsightsofWalmartsInventoryManagementandDemandForecasting/Dashboard3?publish=yes)

### **Members:**
- Michael Nathaniel
- Nadia Nabila Shafira
- Noufal Rifata Reyhan
- Faris Arief Mawardi

### **Description:**
This repository contains a comprehensive project aimed at developing a robust sales forecasting model for Walmart stores. The project utilizes various data such as date, store types, promotions, and environmental factors to forecast sales accurately. The insights derived from this model will assist Walmart's management team in optimizing inventory levels, preventing stock imbalances, and enhancing operational efficiency.

### **Key Features:**
- Detailed data analysis and exploration of Walmart sales data.
- Development and evaluation of sales forecasting models using machine learning and statistical techniques.
- Visualizations and insights showcasing the influential factors affecting sales across Walmart stores.
- Readme file with comprehensive project details, problem statement, objectives, and conclusions.
- Requirements.txt file specifying the necessary dependencies for reproducing the project environment.

### **Contents:**
- Data folder: Contains Walmart sales data and relevant datasets used for analysis.
- Notebooks folder: Includes Notebooks outlining data preprocessing, exploratory data analysis, model development, and evaluation.
- Visualizations folder: Contains graphical representations of insights and correlations.
- README.md: Detailed information about the project, objectives, problem statement, conclusions, and instructions for reproducing the analysis.
- Requirements.txt: Specifies the required dependencies to run the project.

### **Instructions for Use:**
1. Clone the repository to your local machine.
2. Install the necessary dependencies listed in the requirements.txt file.
3. Navigate through the notebooks to understand the data analysis, modeling techniques, and visualizations.
4. Run the notebooks to reproduce the analysis or modify them as per requirements.
5. Refer to the README.md for detailed project insights, conclusions, and recommendations.

### **Conclusion:**

1. **Seasonal Sales Patterns:**
    - **Peak Sales Periods:** Notable sales spikes occur during specific periods like Year-end (November-December), Winter-to-Spring transition (February-March), and Summer months (June-August).
    - **Sales Dips:** Declines are observed during the Spring season (March-May) and the transition from Summer to Fall (August-October).

2. **Impactful Features for Sales Prediction:**
    - Features such as 'Dept', 'Size', 'Store', 'Date', 'Temperature', 'Fuel_Price', 'MarkDown 1-5', 'Unemployment', and 'Type' display higher correlations with 'Weekly_Sales.' These features are crucial for accurate sales forecasting in model development.

3. **Model Performance Insights:**
    - **Training Data Evaluation:** The Random Forest model exhibits robust performance on the training dataset with an R-squared score of 97.74%. The model demonstrates a strong ability to predict outcomes, minimizing errors with a Mean Absolute Error (MAE) of 1406.80 units.
    - **Test Data Evaluation:** On unseen test data, the model maintains commendable performance with an R-squared score of 93.89% and a slightly higher MAE of 2488.92 units. This indicates the model's capacity to generalize well to new data.
    - **Overfitting Consideration:** While a minor overfitting tendency is observed post hyperparameter tuning, it remains within acceptable limits. Continuous monitoring and adjustments are recommended to mitigate potential escalating concerns.
