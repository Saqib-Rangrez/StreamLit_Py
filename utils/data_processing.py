import pandas as pd

def load_uphc_data():
    return pd.read_csv('data/uphc_data.csv')

def filter_children_data(area):
    child_data = pd.read_csv('data/child_data.csv')
    return child_data[child_data['Area'] == area]
