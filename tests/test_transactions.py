from unittest.mock import mock_open, patch

import pandas as pd

from src.transactions import count_fin_transactions_csv, count_fin_transactions_excel


@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data=(
        "id;state;date;amount;currency_name;currency_code;description;from;to\n"
        "1;EXECUTED;2023-01-01;100;RUB;RUB;Payment;Account1;Account2\n"
        "2;PENDING;2023-01-02;200;USD;USD;Transfer;Account3;Account4\n"
    ),
)
def test_count_fin_transactions_csv_success(mock_file):
    result = count_fin_transactions_csv("fake_path.csv")
    expected = [
        {
            "id": "1",
            "state": "EXECUTED",
            "date": "2023-01-01",
            "operationAmount": {"amount": "100", "currency": {"name": "RUB", "code": "RUB"}},
            "description": "Payment",
            "from": "Account1",
            "to": "Account2",
        },
        {
            "id": "2",
            "state": "PENDING",
            "date": "2023-01-02",
            "operationAmount": {"amount": "200", "currency": {"name": "USD", "code": "USD"}},
            "description": "Transfer",
            "from": "Account3",
            "to": "Account4",
        },
    ]
    assert result == expected


@patch("builtins.open", side_effect=FileNotFoundError)
def test_count_fin_transactions_csv_file_not_found(mock_file):
    result = count_fin_transactions_csv("missing.csv")
    assert result == []
    mock_file.assert_called_once_with("missing.csv", encoding="utf8")


@patch("pandas.read_excel")
def test_count_fin_transactions_excel_success(mock_read_excel):
    mock_df = pd.DataFrame(
        {
            "id": [1, 2],
            "state": ["EXECUTED", "PENDING"],
            "date": ["2023-01-01", "2023-01-02"],
            "amount": [100, 200],
            "currency_name": ["RUB", "USD"],
            "currency_code": ["RUB", "USD"],
            "description": ["Payment", "Transfer"],
            "from": ["Account1", "Account3"],
            "to": ["Account2", "Account4"],
        }
    )
    mock_read_excel.return_value = mock_df

    result = count_fin_transactions_excel("fake_path.xlsx")
    expected = [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2023-01-01",
            "operationAmount": {"amount": 100, "currency": {"name": "RUB", "code": "RUB"}},
            "description": "Payment",
            "from": "Account1",
            "to": "Account2",
        },
        {
            "id": 2,
            "state": "PENDING",
            "date": "2023-01-02",
            "operationAmount": {"amount": 200, "currency": {"name": "USD", "code": "USD"}},
            "description": "Transfer",
            "from": "Account3",
            "to": "Account4",
        },
    ]
    assert result == expected


@patch("pandas.read_excel", side_effect=FileNotFoundError)
def test_count_fin_transactions_excel_file_not_found(mock_read_excel):
    result = count_fin_transactions_excel("missing.xlsx")
    assert result == []
    mock_read_excel.assert_called_once_with("missing.xlsx")
