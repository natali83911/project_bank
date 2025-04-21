from datetime import datetime
from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """Функция-декоратор для автоматическго логирования выполнения функций. Принимает необязательный аргумент
    filename, который определяет, куда будут записываться логи (в файл или в консоль)"""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_entry = f"{func.__name__} called at {start_time}\n"

            try:
                result = func(*args, **kwargs)
                status = f"{func.__name__} ok\n"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(log_entry + status)
                else:
                    print(log_entry + status, end="")
                return result
            except Exception as e:
                error_msg = f"{func.__name__} error: {type(e).__name__}. " f"Inputs: {args}, {kwargs}\n"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(log_entry + error_msg)
                else:
                    print(log_entry + error_msg, end="")
                raise

        return wrapper

    return decorator
