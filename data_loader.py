
import pandas as pd

def load_data(file_paths):
    return [pd.read_csv(path) for path in file_paths]