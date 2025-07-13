import pandas as pd

def load_data(url):
    # Carga un archivo 'Parquet' desde una url y lo devuelve como DataFrame.
    df = pd.read_parquet(url)
    return df
