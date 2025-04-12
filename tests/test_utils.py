import json
from unittest.mock import mock_open, patch

from src.utils import load_transactions_from_json


def test_valid_json_file() -> None:
    with patch(
        "builtins.open",
        new_callable=mock_open,
        read_data=json.dumps([{"id": 441945886, "state": "EXECUTED"}, {"id": 41428829, "state": "EXECUTED"}]),
    ):
        transactions = load_transactions_from_json("test_file.json")
        assert isinstance(transactions, list)
        assert len(transactions) == 2


def test_invalid_json() -> None:
    with patch("builtins.open", new_callable=mock_open, read_data="Invalid JSON"):
        transactions = load_transactions_from_json("test_file.json")
        assert isinstance(transactions, list)
        assert len(transactions) == 0


def test_non_list_json() -> None:
    with patch("builtins.open", new_callable=mock_open, read_data='{"key": "value"}'):
        transactions = load_transactions_from_json("test_file.json")
        assert isinstance(transactions, list)
        assert len(transactions) == 0


def test_file_not_found() -> None:
    with patch("builtins.open", side_effect=FileNotFoundError()):
        transactions = load_transactions_from_json("test_file.json")
        assert isinstance(transactions, list)
        assert len(transactions) == 0


def test_empty_json_file() -> None:
    with patch("builtins.open", new_callable=mock_open, read_data="[]"):
        transactions = load_transactions_from_json("test_file.json")
        assert isinstance(transactions, list)
        assert len(transactions) == 0
