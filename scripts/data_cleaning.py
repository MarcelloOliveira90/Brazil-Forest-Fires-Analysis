import pandas as pd

def clean_data(filepath):
    data = pd.read_csv(filepath)
    # Exemplo: Remover valores nulos
    data = data.dropna()
    return data
