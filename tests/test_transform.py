import pandas as pd
from scripts.transform import transform


def test_transform():
    df = pd.DataFrame({"idade": [10, 25, 65]})
    result = transform(df)
    assert list(result["faixa_etaria"]) == ["Jovem", "Adulto", "Idoso"]
