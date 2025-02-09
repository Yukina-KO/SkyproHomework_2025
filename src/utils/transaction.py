import json
import os
import logging
from typing import Any


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
logger = logging.getLogger("src.utils")


def get_transactions() -> Any:
    file_path = os.path.join(BASE_DIR, "data", "operations.json")
    logger.info(f"Читаем транзакции из файла: {file_path}")

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            logger.info(f"Успешно считано транзакций: {len(data)}")
        return data
    except FileNotFoundError:
        logger.error(f"Файл не найден: {file_path}")
    except json.JSONDecodeError as err:
        logger.error(f"Ошибка парсинга JSON: {err}")
