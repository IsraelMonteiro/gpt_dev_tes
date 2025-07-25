from scripts.extract_data import extract

def test_extract():
    df = extract()
    assert not df.empty
    # verify expected columns exist
    assert "nome" in df.columns
    assert "idade" in df.columns
    # DataFrame should have exactly three rows
    assert len(df) == 3
