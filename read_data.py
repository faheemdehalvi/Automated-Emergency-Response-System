import pandas as pd

def read_data():
    data = pd.read_csv('./hospital_data.csv')
    data = data.to_dict('records')
    return data