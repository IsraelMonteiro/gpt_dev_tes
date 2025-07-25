"""Data extraction utilities."""

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class SimpleDataFrame:
    """Very small subset of pandas.DataFrame used in tests."""

    data: Dict[str, List]

    def __post_init__(self) -> None:
        self.columns = list(self.data.keys())
        first_col = next(iter(self.data.values()), [])
        self._size = len(first_col)

    @property
    def empty(self) -> bool:
        return self._size == 0

def extract() -> SimpleDataFrame:
    """Return sample data."""

    data = {
        "nome": ["João", "Maria", "Carlos"],
        "idade": [25, 30, 22],
    }
    return SimpleDataFrame(data)
