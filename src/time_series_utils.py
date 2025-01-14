import numpy as np
import pandas as pd
from statsmodels.tsa.stattools import adfuller, acf, pacf
from sklearn.preprocessing import MinMaxScaler

def check_stationarity(timeseries):
    """
    Perform Augmented Dickey-Fuller test to check stationarity
    """
    result = adfuller(timeseries)
    
    return {
        'test_statistic': result[0],
        'p_value': result[1],
        'critical_values': result[4],
        'is_stationary': result[1] < 0.05
    }

def create_sequences(data, seq_length):
    """
    Create sequences for LSTM input
    """
    xs, ys = [], []
    for i in range(len(data) - seq_length):
        x = data[i:(i + seq_length)]
        y = data[i + seq_length]
        xs.append(x)
        ys.append(y)
    return np.array(xs), np.array(ys)

def compute_autocorrelation(data, nlags=40):
    """
    Compute ACF and PACF
    """
    acf_values = acf(data, nlags=nlags)
    pacf_values = pacf(data, nlags=nlags)
    
    return acf_values, pacf_values

def scale_data(data):
    """
    Scale data to (-1, 1) range
    """
    scaler = MinMaxScaler(feature_range=(-1, 1))
    scaled_data = scaler.fit_transform(data.reshape(-1, 1))
    return scaled_data, scaler