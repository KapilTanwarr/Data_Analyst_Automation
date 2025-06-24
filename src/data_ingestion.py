
import pandas as pd

def load_data(path):
    try:
        df = pd.read_csv(path)
        return df
    except Exception as e:
        raise Exception(f"Failed to load data: {e}")
