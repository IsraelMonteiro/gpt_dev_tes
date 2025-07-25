import pandas as pd

def transform(df: pd.DataFrame) -> pd.DataFrame:
    """Adiciona a coluna `faixa_etaria` ao DataFrame."""
    def classificar(idade: int) -> str:
        if idade < 18:
            return "Jovem"
        if idade < 60:
            return "Adulto"
        return "Idoso"

    novo_df = df.copy()
    novo_df["faixa_etaria"] = novo_df["idade"].apply(classificar)
    return novo_df
