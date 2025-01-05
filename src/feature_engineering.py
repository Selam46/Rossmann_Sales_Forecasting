import pandas as pd
def generate_date_features(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df['Weekday'] = df['Date'].dt.weekday
    df['IsWeekend'] = df['Weekday'] >= 5
    df['Month'] = df['Date'].dt.month
    df['Year'] = df['Date'].dt.year
    df['Day'] = df['Date'].dt.day
    df['DaysToHoliday'] = (pd.to_datetime('2025-12-25') - df['Date']).dt.days
    return df
