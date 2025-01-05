def handle_missing_values(train, test, store):
    """
    Handle missing values for numeric and non-numeric columns.
    """
    # Handle numeric columns: Fill NaNs with the median
    for df in [train, test, store]:
        numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
    
    # Handle non-numeric columns: Fill NaNs with 'Unknown'
    for df in [train, test, store]:
        non_numeric_cols = df.select_dtypes(include=['object']).columns
        df[non_numeric_cols] = df[non_numeric_cols].fillna('Unknown')
    
    return train, test, store
