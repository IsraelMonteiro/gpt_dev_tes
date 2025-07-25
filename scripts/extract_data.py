import pandas as pd

def extract():
    # Simula extração de dados
    df = pd.DataFrame({
        "nome": ["João", "Maria", "Carlos"],
        "idade": [25, 30, 22]
    })
    return df
