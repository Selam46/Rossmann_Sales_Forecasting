### eda_utils.py
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def plot_distribution(df, column, title, xlabel, ylabel):
    """Plot the distribution of a given column."""
    sns.histplot(df[column], kde=True)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


def plot_correlation(df, title="Correlation Heatmap"):
    """Plot correlation heatmap for a dataframe."""
    correlation = df.corr()
    sns.heatmap(correlation, annot=True, cmap="coolwarm")
    plt.title(title)
    plt.show()


def plot_sales_trends(df, date_col, sales_col):
    """Visualize sales trends over time."""
    df[date_col] = pd.to_datetime(df[date_col])
    sales_trends = df.groupby(date_col)[sales_col].sum().reset_index()

    plt.figure(figsize=(15, 5))
    sns.lineplot(x=date_col, y=sales_col, data=sales_trends)
    plt.title("Sales Trends Over Time")
    plt.xlabel("Date")
    plt.ylabel("Total Sales")
    plt.show()



