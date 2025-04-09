from typing import Any

from src.decorators import log


def test_file_logging_success() -> None:
    file_path = "mylog.txt"  # Указываем путь к файлу как строку

    @log(filename=file_path)
    def add(a: int, b: int) -> int:
        return a + b

    # Вызываем функцию
    add(2, 3)

    # Читаем содержимое файла
    with open(file_path) as f:
        content = f.read()

    # Проверяем, что лог содержит успешное выполнение
    assert "add ok" in content


def test_file_logging_error() -> None:
    file_path = "mylog.txt"  # Указываем путь к файлу как строку

    @log(filename=file_path)
    def fail_func() -> Any:
        raise ValueError("Test error")

    # Вызываем функцию и обрабатываем исключение
    try:
        fail_func()
    except ValueError:
        pass

    # Читаем содержимое файла
    with open(file_path) as f:
        content = f.read()

    # Проверяем, что лог содержит информацию об ошибке
    assert "fail_func error: ValueError" in content
    assert "Inputs: (), {}" in content


def test_console_logging(capsys: Any) -> None:
    @log()
    def multiply(x: int, y: int) -> int:
        return x * y

    multiply(3, 4)
    captured = capsys.readouterr()
    assert "multiply ok" in captured.out
