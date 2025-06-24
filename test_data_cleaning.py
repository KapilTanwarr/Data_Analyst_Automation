
import pandas as pd
from src.data_cleaning import clean_data

def test_clean_data():
    raw = pd.DataFrame({
        ' Name ': ['A', 'B', None],
        ' Age ': [25, None, 30]
    })
    cleaned = clean_data(raw)
    assert 'name' in cleaned.columns
    assert cleaned.shape[0] == 1
