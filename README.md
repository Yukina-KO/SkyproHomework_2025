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
│   │   ├── get_date.py
│   │   ├── mask_account_card.py
│   ├── processing/
│       ├── test_masks.py
│       ├── test_processing.py
│       ├── test_widget.py
└── README.md
```

---

## Тесты

### Маскировка информации (`test_masks.py`)
Тесты для функций `get_mask_account` и `get_mask_card_number`. Основные сценарии:
- Проверка корректного маскирования.
- Обработка некорректных данных (пустые строки, неправильная длина, нецифровые символы).
- Параметризованные тесты для различных случаев.

Пример параметризованного теста:
```python
@pytest.mark.parametrize("account_number, expected", [
    ("12345678901234567890", "**7890"),
    ("12345678", "Некорректный номер"),
    ("1234abcd567890123456", "Некорректный номер"),
    ("abcd1234567890123456", "Некорректный номер")
])
def test_get_mask_account_parametrized(account_number, expected):
    assert get_mask_account(account_number) == expected
```

### Обработка данных (`test_processing.py`)
Тесты для функций `filter_by_state` и `sort_by_date`. Основные сценарии:
- Фильтрация по статусу с различными наборами данных (простой, пустой, с дубликатами).
- Сортировка по дате (по возрастанию и убыванию).
- Проверка обработки некорректных дат.
- Использование фикстур для подготовки тестовых данных.

Пример теста сортировки:
```python
@pytest.mark.parametrize("fixture_name, sort_increase, expected", [
    ("test_data_simple", True, [
        {"state": "EXECUTED", "date": "2023-01-01T12:00:00", "data": 1},
        {"state": "CANCELED", "date": "2023-01-02T12:00:00", "data": 2},
        {"state": "PENDING", "date": "2023-01-03T12:00:00", "data": 3},
        {"state": "EXECUTED", "date": "2023-01-04T12:00:00", "data": 4}
    ]),
    ("test_data_empty", True, [])
])
def test_sort_by_date(fixture_name, sort_increase, expected, request):
    input_list = request.getfixturevalue(fixture_name)
    assert sort_by_date(input_list, sort_increase) == expected
```

### Виджет (`test_widget.py`)
Тесты для функций `mask_account_card` и `get_date`. Основные сценарии:
- Проверка корректного преобразования дат.
- Обработка некорректных форматов даты.
- Маскирование номеров карт и счетов с различными форматами.
- Параметризованные тесты для универсальности.

Пример теста преобразования даты:
```python
@pytest.mark.parametrize("date, expected", [
    ("2023-01-01", "01.01.2023"),
    ("1999-12-31", "31.12.1999"),
    ("20-01-01", "Неверный формат даты")
])
def test_get_date_parametrized(date, expected):
    assert get_date(date) == expected
```

---

Для запуска тестов используйте:
```bash
pytest src/processing/test_masks.py
pytest src/processing/test_processing.py
pytest src/processing/test_widget.py
```


