# Rossmann Store Sales Prediction and Deployment

This project focuses on predicting daily sales for Rossmann stores across multiple cities using machine learning and deploying the models for real-time usage. It covers data exploration, preprocessing, modeling, post-prediction analysis, and deployment-ready pipelines.

---

## **Project Overview**

### **Goal**
Forecast sales for Rossmann stores up to six weeks in advance, enabling better planning and decision-making.

### **Key Tasks**
1. **Exploration of Customer Purchasing Behavior (Task 1)**:
   - Perform Exploratory Data Analysis (EDA) to understand trends, patterns, and the impact of factors like promotions, holidays, and store types.
   - Visualize insights for actionable recommendations.

2. **Prediction of Store Sales (Task 2)**:
   - **Preprocessing (Task 2.1)**: Prepare the data with imputation, encoding, and scaling.
   - **Model Building (Task 2.2)**: Use `RandomForestRegressor` with `sklearn` pipelines for modularity.
   - **Loss Function (Task 2.3)**: Evaluate model performance with `Mean Absolute Error (MAE)`.
   - **Post-Prediction Analysis (Task 2.4)**: Analyze feature importance and calculate confidence intervals.
   - **Model Serialization (Task 2.5)**: Save models with timestamps for tracking.

3. **Deep Learning for Sales Prediction (Task 3)**:
   - Build and evaluate an LSTM model for time series forecasting.
   - Explore advanced techniques like autocorrelation and stationarity testing.


---

## **How to Run the Project**

1. **Environment Setup**:
   - Clone the repository and navigate to the project directory:
     ```bash
     git clone <repository_url>
     cd <repository_folder>
     ```
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```

2. **Run Notebooks**:
   - Notebooks for each task are in the `notebooks/` directory. Open and execute them sequentially:
     ```bash
     jupyter notebook notebooks/<notebook_name>.ipynb
     ```