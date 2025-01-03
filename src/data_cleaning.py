### data_cleaning.py
import logging
import pandas as pd
import numpy as np
from datetime import datetime
from logging_config import setup_logger

# Clean Data Function
def clean_data(train_df, store_df):
    """Clean and preprocess the dataframes."""

    # Logging setup
    logger = setup_logger("cleaning_logger", "../logs/cleaning.log")

    # Fill missing CompetitionDistance with mean
    if 'CompetitionDistance' in store_df.columns:
        store_df['CompetitionDistance'].fillna(store_df['CompetitionDistance'].mean(), inplace=True)
        logger.info("Filled missing CompetitionDistance with mean.")

    # Fill missing CompetitionOpenSince with placeholder values
    store_df['CompetitionOpenSinceYear'].fillna(2000, inplace=True)
    store_df['CompetitionOpenSinceMonth'].fillna(1, inplace=True)
    logger.info("Filled missing competition opening data with placeholders.")

    # Convert StateHoliday column to consistent format
    train_df['StateHoliday'] = train_df['StateHoliday'].replace({0: 'None'})
    logger.info("Standardized StateHoliday values.")

    # Create competition age feature
    store_df['CompetitionAge'] = ((datetime.now().year - store_df['CompetitionOpenSinceYear']) * 12 +
                                  (datetime.now().month - store_df['CompetitionOpenSinceMonth']))
    store_df['CompetitionAge'].fillna(0, inplace=True)
    logger.info("Created CompetitionAge feature.")

    return train_df, 
def setup_logger(name, log_file, level=logging.INFO):
    """Setup logger for consistent logging."""
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger