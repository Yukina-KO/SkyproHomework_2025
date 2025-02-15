import logging
import os
import sys

from src.masks.masks import get_mask_account, get_mask_card_number
from src.utils.transaction import get_transactions

# Определяем корневую директорию проекта (на уровень выше текущего файла).
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Убеждаемся, что она в sys.path, чтобы корректно импортировать src.*
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

# Создаём папку logs (если не существует).
logs_dir = os.path.join(BASE_DIR, "logs")
os.makedirs(logs_dir, exist_ok=True)

# НАСТРОЙКА ЛОГЕРА ДЛЯ МОДУЛЯ utils
utils_logger = logging.getLogger("src.utils")
utils_logger.setLevel(logging.DEBUG)

utils_log_path = os.path.join(logs_dir, "utils.log")
utils_file_handler = logging.FileHandler(utils_log_path, mode="w", encoding="utf-8")
utils_file_handler.setLevel(logging.DEBUG)

# Формат лога: время, имя логгера, уровень, сообщение
utils_file_formatter = logging.Formatter("%(asctime)s [%(name)s] %(levelname)s: %(message)s")
utils_file_handler.setFormatter(utils_file_formatter)

# «Подключаем» хендлер к логеру
utils_logger.addHandler(utils_file_handler)

# НАСТРОЙКА ЛОГЕРА ДЛЯ МОДУЛЯ masks
masks_logger = logging.getLogger("src.masks")
masks_logger.setLevel(logging.DEBUG)

masks_log_path = os.path.join(logs_dir, "masks.log")
masks_file_handler = logging.FileHandler(masks_log_path, mode="w", encoding="utf-8")
masks_file_handler.setLevel(logging.DEBUG)

masks_file_formatter = logging.Formatter("%(asctime)s [%(name)s] %(levelname)s: %(message)s")
masks_file_handler.setFormatter(masks_file_formatter)

masks_logger.addHandler(masks_file_handler)


# Тестируем работу
def run_logging() -> None:
    transactions = get_transactions()
    masked_card = get_mask_card_number("1111222233334441")
    masked_acc = get_mask_account("12345678901234567890")

    print("Маскированная карта:", masked_card)
    print("Маскированный счёт:", masked_acc)
    print("Считанные транзакции:", transactions)


run_logging()
