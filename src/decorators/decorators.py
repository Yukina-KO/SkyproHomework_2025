import logging
import functools
import sys
from typing import Callable, Any, Optional


def log(filename: Optional[str] = None) -> Callable:
    logger = logging.getLogger("function_logger")
    logger.setLevel(logging.INFO)

    # Удаляем все существующие обработчики
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    if filename:
        handler = logging.FileHandler(filename, mode='a', encoding='utf-8')
    else:
        # Явно указываем, что StreamHandler выводит в stdout
        handler = logging.StreamHandler(sys.stdout)

    # Упрощенный формат логов (без временных меток)
    formatter = logging.Formatter('%(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                logger.info(f"Начало выполнения функции {func.__name__} с аргументами: {args}, {kwargs}")
                result = func(*args, **kwargs)
                logger.info(f"Функция {func.__name__} завершена. Результат: {result}")
                return result
            except Exception as e:
                logger.error(f"Ошибка в функции {func.__name__}: {type(e).__name__} - {e}. "
                             f"Аргументы: {args}, {kwargs}")
                raise
            finally:
                logger.info(f"Завершение выполнения функции {func.__name__}")
                logger.handlers[0].flush()  # Сбрасываем буфер
        return wrapper
    return decorator
