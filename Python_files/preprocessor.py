import pandas as pd

def clean_data(data):
    """
    Cleans the input DataFrame by performing the following steps:
    - Removes the 'Unnamed: 0' column if present.
    - Converts player height from cm to meters.
    - Flags invalid player heights (>2.5m), weights (>200kg), and ages (<18).

    Parameters:
    data (pd.DataFrame): Input DataFrame containing NBA players data.

    Returns:
    pd.DataFrame: Cleaned DataFrame.
    dict: Dictionary containing DataFrames of invalid entries (optional).
    """
    # Remove the 'Unnamed: 0' column if it exists
    if 'Unnamed: 0' in data.columns:
        data.drop(columns=['Unnamed: 0'], inplace=True)

    # Convert player height from cm to meters
    data['player_height'] = data['player_height'] / 100

    # Identify invalid entries
    invalid_heights = data[data['player_height'] > 2.5]
    invalid_weights = data[data['player_weight'] > 200]
    invalid_ages = data[data['age'] < 18]

    # Remove invalid entries from the dataset (comment this out if not needed)
    data = data[(data['player_height'] <= 2.5) & 
                (data['player_weight'] <= 200) & 
                (data['age'] >= 18)]

    # Return the cleaned data and invalid entries as a dictionary (optional)
    return data

    # return data, {
    #    'invalid_heights': invalid_heights,
    #    'invalid_weights': invalid_weights,
    #    'invalid_ages': invalid_ages
    #}
