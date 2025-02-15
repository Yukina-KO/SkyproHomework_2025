from typing import Dict, Hashable, List
from unittest.mock import MagicMock, patch

from src.transactions.transactions import read_transactions_csv, read_transactions_excel


@patch("src.transactions.transactions.pd.read_csv")
def test_read_transactions_csv(mock_read_csv: MagicMock) -> None:
    """
    Тест на функцию read_transactions_csv с использованием mock для pd.read_csv.
    """
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [
        {"id": "123", "amount": "100", "currency": "RUB"},
        {"id": "456", "amount": "200", "currency": "USD"},
    ]
    mock_read_csv.return_value = mock_df

    result: List[Dict[Hashable, str]] = read_transactions_csv("fake/path/transactions.csv")

    assert len(result) == 2
    assert result[0]["id"] == "123"
    assert result[1]["currency"] == "USD"

    mock_read_csv.assert_called_once_with("fake/path/transactions.csv", sep=";")

    mock_df.to_dict.assert_called_once_with(orient="records")


@patch("src.transactions.transactions.pd.read_excel")
def test_read_transactions_excel(mock_read_excel: MagicMock) -> None:
    """
    Тест на функцию read_transactions_excel с использованием mock для pd.read_excel.
    """
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [{"id": "789", "amount": "500", "currency": "EUR"}]
    mock_read_excel.return_value = mock_df

    result: List[Dict[Hashable, str]] = read_transactions_excel("fake/path/transactions.xlsx")

    assert len(result) == 1
    assert result[0]["id"] == "789"
    assert result[0]["currency"] == "EUR"

    mock_read_excel.assert_called_once_with("fake/path/transactions.xlsx")
    mock_df.to_dict.assert_called_once_with(orient="records")
