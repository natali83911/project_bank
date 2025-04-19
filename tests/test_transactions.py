from unittest.mock import mock_open, patch

import pandas as pd

from src.transactions import count_fin_transactions_csv, count_fin_transactions_excel


@patch("builtins.open", new_callable=mock_open, read_data="col1;col2\nval1;val2\nval3;val4\n")
def test_count_fin_transactions_csv_success(mock_file):
    result = count_fin_transactions_csv("fake_path.csv")
    expected = [{"col1": "val1", "col2": "val2"}, {"col1": "val3", "col2": "val4"}]
    assert result == expected
    mock_file.assert_called_once_with("fake_path.csv", encoding="utf8")


@patch("builtins.open", side_effect=FileNotFoundError)
def test_count_fin_transactions_csv_file_not_found(mock_file):
    result = count_fin_transactions_csv("missing.csv")
    assert result == []
    mock_file.assert_called_once_with("missing.csv", encoding="utf8")


@patch("pandas.read_excel")
def test_count_fin_transactions_excel_success(mock_read_excel):
    mock_df = pd.DataFrame([{"col1": "val1", "col2": "val2"}, {"col1": "val3", "col2": "val4"}])
    mock_read_excel.return_value = mock_df

    result = count_fin_transactions_excel("fake_path.xlsx")
    expected = [{"col1": "val1", "col2": "val2"}, {"col1": "val3", "col2": "val4"}]
    assert result == expected
    mock_read_excel.assert_called_once_with("fake_path.xlsx")


@patch("pandas.read_excel", side_effect=FileNotFoundError)
def test_count_fin_transactions_excel_file_not_found(mock_read_excel):
    result = count_fin_transactions_excel("missing.xlsx")
    assert result == []
    mock_read_excel.assert_called_once_with("missing.xlsx")
