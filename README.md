## Описание
Этот проект включает простые инструменты для обработки и организации данных. Основные функции:
- Фильтрация данных по статусу.
- Сортировка данных по дате.
- Сокрытие чувствительной информации (счета и карты).
- Форматирование дат для удобного чтения.
- Фильтрация данных по валюте.
- Генерация описаний транзакций.
- Генерация номеров карт в заданном диапазоне.
- Логирование вызовов функций.

---

## Возможности

### 1. Фильтрация данных по статусу
Фильтрует список словарей по заданному статусу (EXECUTED или CANCELED).

**Функция**: `filter_by_state`
```python
filter_by_state(input_list: List[Dict], state_default: str = "EXECUTED") -> List[Dict]
```

### 2. Сортировка данных по дате
Сортирует список словарей по полю `date` (по возрастанию или убыванию).

**Функция**: `sort_by_date`
```python
sort_by_date(input_list: List[Dict], sort_increase: bool = True) -> List[Dict]
```

### 3. Сокрытие чувствительной информации
Скрывает номера счетов или карт для безопасности.

**Функция**: `mask_account_card`
```python
mask_account_card(account_card: str) -> str
```

### 4. Форматирование дат
Преобразует дату из формата ISO в ДД.ММ.ГГГГ для удобного чтения.

**Функция**: `get_date`
```python
get_date(date: str) -> str
```

### 5. Фильтрация данных по валюте
Фильтрует список транзакций по заданному коду валюты.

**Функция**: `filter_by_state`
```python
filter_by_state(input_list: List[Dict], currency: str) -> Generator[dict, None, None]
```

### 6. Генерация описаний транзакций
Генерирует описания для каждого элемента из списка транзакций.

**Функция**: `transaction_descriptions`
```python
transaction_descriptions(input_list: List[Dict]) -> Generator[str, None, None]
```

### 7. Генерация номеров карт
Создает номера карт в заданном диапазоне в формате `XXXX XXXX XXXX XXXX`.

**Функция**: `card_number_generator`
```python
card_number_generator(start: int, end: int) -> Generator[str, None, None]
```

### 8. Логирование вызовов функций
Логирует вызов обёрнутой функции, включая:
- Имя функции и переданные аргументы (позиционные и именованные);
- Успешное завершение с указанием результата;
- Ошибки с типом исключения и сообщением.

#### Возможности:
- Если указан путь к файлу, логи записываются в этот файл (в случае его существования). Иначе логи выводятся в консоль.
- Логи автоматически сбрасываются после каждой операции.

**Функция**: `log`
```python
@log(filename: Optional[str] = None) -> Callable
```
Пример использования:
```python
@log("log.txt")
def example_function(x: int, y: int) -> int:
    return x + y

result = example_function(1, 2)
```

---

## Установка

Создайте файл `.env` в корне проекта, добавьте в него переменную окружения `API_KEY` со значением, полученным на [apilayer.com](https://apilayer.com/exchangerates_data-api).  
   Пример:
   ```bash
   API_KEY=SljP4YdU5F1gLm6Vdv4fj39GAE2oKA2a
   ```



---

## Структура файлов

```
project/
├── data/
│   ├── operations.json/
├── src/
│   ├── decorators/
│   │   ├── decorators.py
│   ├── external_api/
│   │   ├── external_api.py
│   ├── generators/
│   │   ├── filter_by_state.py
│   │   ├── transaction_descriptions.py
│   │   ├── card_number_generator.py
│   ├── masks/
│   │   ├── get_mask_account.py
│   │   ├── get_mask_card_number.py
│   ├── processing/
│   │   ├── filter_by_state.py
│   │   ├── sort_by_date.py
│   ├── utils/
│   │   ├── transaction.py
│   ├── widget/
│   │   ├── get_date.py
│   │   ├── mask_account_card.py
│── tests/
│   ├── test_decorators.py
│   ├── test_generators.py
│   ├── test_masks.py
│   ├── test_processing.py
│   ├── test_ransactions.py
│   ├── test_widget.py
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

### Декораторы (`test_decorators.py`)

#### Основные сценарии:
- Логирование в консоль (при отсутствии файла).
- Логирование в файл (при наличии пути).
- Обработка ошибок.
- Логирование аргументов.
- Сохранение метаданных функции.

Пример теста логирования в файл:

```python
def test_log_file_output():
    log_file = "test_log.txt"
    if not os.path.exists(log_file):
        with open(log_file, "w", encoding="utf-8"):
            pass

    @log(filename=log_file)
    def test_function(x: int, y: int) -> int:
        return x + y

    test_function(1, 2)

    with open(log_file, "r", encoding="utf-8") as f:
        log_content = f.read()
        assert "Начало выполнения функции test_function с аргументами: (1, 2), {}" in log_content
        assert "Функция test_function завершена. Результат: 3" in log_content
```

---

Для запуска тестов используйте:

```bash
pytest tests/test_masks.py
pytest tests/test_processing.py
pytest tests/test_widget.py
pytest tests/test_generators.py
pytest tests/test_decorators.py
pytest tests/test_transactions.py