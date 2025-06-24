
def clean_data(df):
    df.dropna(inplace=True)
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    return df
