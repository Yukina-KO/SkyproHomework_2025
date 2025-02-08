import functools
import logging
import os
import sys
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор, который логирует вызов обёрнутой функции:
      - Если указан путь к файлу и файл существует, записи добавляются в этот файл;
      - Если файл не существует или путь к файлу не передан, логи выводятся в консоль.

    Логируются:
      • Начало выполнения (имя функции, позиционные и именованные аргументы);
      • Успешное завершение (результат функции);
      • Ошибки (тип исключения, текст ошибки).
    После каждой операции буфер лога сбрасывается.
    """
    logger = logging.getLogger("function_logger")
    logger.setLevel(logging.INFO)
    # Удаляю все существующие обработчики
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    if filename:
        if os.path.exists(filename):
            handler = logging.FileHandler(filename, mode="a", encoding="utf-8")
        else:
            handler = logging.StreamHandler(sys.stdout)
    else:
        handler = logging.StreamHandler(sys.stdout)

    # # Упрощенный формат логов (без временных меток)
    formatter = logging.Formatter("%(message)s")
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
                logger.error(
                    f"Ошибка в функции {func.__name__}: {type(e).__name__} - {e}. " f"Аргументы: {args}, {kwargs}"
                )
                raise
            finally:
                logger.info(f"Завершение выполнения функции {func.__name__}")
                logger.handlers[0].flush()  # Сбрасываю буфер

        return wrapper

    return decorator
