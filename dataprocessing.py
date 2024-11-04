import pandas as pd

def load_and_clean_data(file_path):
    df = pd.read_csv(file_path)
    df.dropna(inplace=True)
    df = df[df['distance'] > 0]
    return df
