## Описание
Этот проект включает простые инструменты для обработки и организации данных. Основные функции:
- Фильтрация данных по статусу.
- Сортировка данных по дате.
- Сокрытие чувствительной информации (счета и карты).
- Форматирование дат для удобного чтения.

---

## Возможности

### 1. Фильтрация данных по статусу
Фильтрует список словарей по заданному статусу (`EXECUTED` или `CANCELED`).

Функция: `filter_by_state`
```python
filter_by_state(input_list: List[Dict], state_default: str = "EXECUTED") -> List[Dict]
```

### 2. Сортировка данных по дате
Сортирует список словарей по полю `date` (по возрастанию или убыванию).

Функция: `sort_by_date`
```python
sort_by_date(input_list: List[Dict], sort_increase: bool = True) -> List[Dict]
```

### 3. Сокрытие чувствительной информации
Скрывает номера счетов или карт для безопасности.

Функция: `mask_account_card`
```python
mask_account_card(account_card: str) -> str
```

### 4. Форматирование дат
Преобразует дату из формата ISO в `ДД.ММ.ГГГГ` для удобного чтения.

Функция: `get_date`
```python
get_date(date: str) -> str
```

---

## Примеры использования

### Входные данные
```python
transactions = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
```

### Фильтрация по статусу
```python
executed_transactions = filter_by_state(transactions, "EXECUTED")
```

### Сортировка по дате
```python
sorted_transactions = sort_by_date(transactions, True)
```

### Сокрытие информации
```python
masked_card = mask_account_card("Maestro 1596837868705199")
masked_account = mask_account_card("Счет 64686473678894779589")
```

### Форматирование даты
```python
formatted_date = get_date("2024-03-11T02:26:18.671407")
```

---

## Установка

1. Склонируйте репозиторий:
```bash
git clone <repository-url>
cd <repository-folder>
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

---

## Структура файлов
```
project/
├── src/
│   ├── masks/
│   │   ├── get_mask_account.py
│   │   ├── get_mask_card_number.py
│   ├── processing/
│   │   ├── filter_by_state.py
│   │   ├── sort_by_date.py
│   ├── widget/
│       ├── get_date.py
│       ├── mask_account_card.py
└── README.md
```
