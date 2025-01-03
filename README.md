# Customer Purchasing Behavior Exploration

This project explores customer purchasing behavior across various stores at **Rossmann Pharmaceuticals** through an exploratory data analysis (EDA). The goal is to analyze how factors such as promotions, competition, and holidays influence sales.

## Project Overview

### Task 1: Exploration of Customer Purchasing Behavior

The objectives of this task are:

- **Data Cleaning:** Build pipelines to detect and handle outliers and missing data to ensure accurate analysis.
- **Exploratory Data Analysis:** Visualize and analyze various features to uncover insights into customer behavior.

### Key Questions Explored

1. **Distribution Analysis:**
   - Are promotions distributed similarly between training and test sets?
  
2. **Sales Behavior:**
   - How do sales behave before, during, and after holidays?
   - Are there seasonal purchase behaviors (e.g., Christmas, Easter)?

3. **Correlation Analysis:**
   - What is the correlation between sales and the number of customers?
   - How do promotions affect sales? Are they attracting more customers?

4. **Promo Deployment:**
   - Which stores should promotions be deployed in for maximum effectiveness?

5. **Customer Behavior Trends:**
   - Analyze customer behavior during store opening and closing times.
   - How do weekdays affect weekend sales for stores open all week?

6. **Assortment Type and Competitor Distance:**
   - How does the assortment type affect sales?
   - What impact does the distance to the nearest competitor have on sales?
   - How do new competitors affect stores with previously unknown competitor distances?

### Deliverables

- An exploratory analysis notebook that answers all the questions using appropriate plots and summary tables.
- Logging of all steps using the `logger` library in Python for traceability and reproducibility.

## Getting Started

To run this project, clone the repository and navigate to the project directory:

```bash
git clone https://github.com/Selam46/Rossmann_Sales_Forecasting.git
cd <project-directory>

Install the required dependencies:
pip install -r requirements.txt