from scripts.extract_data import extract

def test_extract():
    df = extract()
    assert not df.empty
    assert "nome" in df.columns
