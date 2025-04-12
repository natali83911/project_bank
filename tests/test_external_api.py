from typing import Any, Dict, Optional, Union
from unittest.mock import MagicMock, Mock, patch

import requests

from src.external_api import convert_to_rub


# Функция для мокирования API-ответа
def create_mock_response(json_data: Dict[str, Any], status_code: int) -> MagicMock:
    """Создает мок-объект ответа."""
    mock_response = MagicMock()
    mock_response.json.return_value = json_data
    mock_response.status_code = status_code
    return mock_response


def test_rub_transaction() -> None:
    """Проверяет, что функция правильно обрабатывает транзакции в рублях (RUB)."""
    transaction: Dict[str, Any] = {"operationAmount": {"amount": "31957.58", "currency": {"code": "RUB"}}}
    result: Optional[Union[float, int]] = convert_to_rub(transaction)
    assert result == 31957.58


@patch("requests.get")
def test_usd_transaction(mock_get: MagicMock) -> None:
    """Проверяет, что функция правильно обрабатывает транзакции в долларах (USD), мокируя API-запрос."""
    transaction: Dict[str, Any] = {"operationAmount": {"amount": "8221.37", "currency": {"code": "USD"}}}
    mock_response = create_mock_response({"result": 750000.00}, 200)
    mock_get.return_value = mock_response
    result: Optional[Union[float, int]] = convert_to_rub(transaction)
    assert result == 750000.00
    mock_get.assert_called_once()


def test_invalid_amount() -> None:
    """Проверяет, что функция правильно обрабатывает неверный формат суммы (`amount`)."""
    transaction: Dict[str, Any] = {"operationAmount": {"amount": "invalid", "currency": {"code": "USD"}}}
    result: Optional[Union[float, int]] = convert_to_rub(transaction)
    assert result is None


def test_missing_amount() -> None:
    """Проверяет, что функция обрабатывает отсутствие суммы (`amount`)."""
    transaction: Dict[str, Any] = {"operationAmount": {"currency": {"code": "USD"}}}
    result: Optional[Union[float, int]] = convert_to_rub(transaction)
    assert result is None


@patch("requests.get")
def test_api_failure(mock_get: MagicMock) -> None:
    """Проверяет, что функция правильно обрабатывает ошибки API."""
    transaction: Dict[str, Any] = {"operationAmount": {"amount": "100.00", "currency": {"code": "USD"}}}
    mock_response = Mock()
    mock_response.raise_for_status.side_effect = requests.exceptions.RequestException("API Error")
    mock_get.return_value = mock_response

    result: Optional[Union[float, int]] = convert_to_rub(transaction)
    assert result is None


@patch("requests.get")
def test_connection_error(mock_get: MagicMock) -> None:
    """Проверяет, что функция правильно обрабатывает ошибки соединения."""
    transaction: Dict[str, Any] = {"operationAmount": {"amount": "100.00", "currency": {"code": "USD"}}}
    mock_get.side_effect = requests.exceptions.RequestException("Connection Error")

    result: Optional[Union[float, int]] = convert_to_rub(transaction)
    assert result is None


if __name__ == "__main__":
    test_rub_transaction()
    test_usd_transaction()
    test_invalid_amount()
    test_missing_amount()
    test_api_failure()
    test_connection_error()
