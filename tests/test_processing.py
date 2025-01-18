import pytest
from src.processing.processing import filter_by_state, sort_by_date


# Фикстуры для тестовых данных
@pytest.fixture
def test_data_simple():
    """
    Простые тестовые данные с базовыми случаями.
    """
    return [
        {"state": "EXECUTED", "date": "2023-01-01T12:00:00", "data": 1},
        {"state": "CANCELED", "date": "2023-01-02T12:00:00", "data": 2},
        {"state": "PENDING", "date": "2023-01-03T12:00:00", "data": 3},
        {"state": "EXECUTED", "date": "2023-01-04T12:00:00", "data": 4}
    ]


@pytest.fixture
def test_data_duplicates():
    """
    Тестовые данные с дублирующимися датами и состояниями.
    """
    return [
        {"state": "EXECUTED", "date": "2023-01-01T12:00:00", "data": 1},
        {"state": "EXECUTED", "date": "2023-01-01T12:00:00", "data": 2},
        {"state": "CANCELED", "date": "2023-01-02T12:00:00", "data": 3},
        {"state": "CANCELED", "date": "2023-01-02T12:00:00", "data": 4}
    ]


@pytest.fixture
def test_data_mixed_states():
    """
    Тестовые данные с различными состояниями и датами.
    """
    return [
        {"state": "EXECUTED", "date": "2023-01-01T12:00:00", "data": 1},
        {"state": "CANCELED", "date": "2023-01-05T12:00:00", "data": 2},
        {"state": "PENDING", "date": "2023-01-03T12:00:00", "data": 3},
        {"state": "EXECUTED", "date": "2023-01-04T12:00:00", "data": 4},
        {"state": "CANCELED", "date": "2023-01-02T12:00:00", "data": 5}
    ]


@pytest.fixture
def test_data_invalid_dates():
    """
    Тестовые данные с некорректными и корректными датами.
    """
    return [
        {"state": "EXECUTED", "date": "invalid-date", "data": 1},
        {"state": "CANCELED", "date": "2023-01-02T12:00:00", "data": 2},
        {"state": "PENDING", "date": "not-a-date", "data": 3},
        {"state": "EXECUTED", "date": "2023-01-04T12:00:00", "data": 4}
    ]


@pytest.fixture
def test_data_empty():
    """
    Пустой список для проверки работы с пустыми данными.
    """
    return []


# Тесты для filter_by_state
@pytest.mark.parametrize("fixture_name, state_default, expected", [
    ("test_data_simple", "EXECUTED", [
        {"state": "EXECUTED", "date": "2023-01-01T12:00:00", "data": 1},
        {"state": "EXECUTED", "date": "2023-01-04T12:00:00", "data": 4}
    ]),
    ("test_data_duplicates", "CANCELED", [
        {"state": "CANCELED", "date": "2023-01-02T12:00:00", "data": 3},
        {"state": "CANCELED", "date": "2023-01-02T12:00:00", "data": 4}
    ]),
    ("test_data_mixed_states", "PENDING", [
        {"state": "PENDING", "date": "2023-01-03T12:00:00", "data": 3}
    ]),
    ("test_data_empty", "EXECUTED", [])
])
def test_filter_by_state(fixture_name, state_default, expected, request):
    """Тесты фильтрации по state_default с использованием фикстур."""
    input_list = request.getfixturevalue(fixture_name)
    assert filter_by_state(input_list, state_default) == expected


# Тесты для sort_by_date
@pytest.mark.parametrize("fixture_name, sort_increase, expected", [
    ("test_data_simple", True, [
        {"state": "EXECUTED", "date": "2023-01-01T12:00:00", "data": 1},
        {"state": "CANCELED", "date": "2023-01-02T12:00:00", "data": 2},
        {"state": "PENDING", "date": "2023-01-03T12:00:00", "data": 3},
        {"state": "EXECUTED", "date": "2023-01-04T12:00:00", "data": 4}
    ]),
    ("test_data_simple", False, [
        {"state": "EXECUTED", "date": "2023-01-04T12:00:00", "data": 4},
        {"state": "PENDING", "date": "2023-01-03T12:00:00", "data": 3},
        {"state": "CANCELED", "date": "2023-01-02T12:00:00", "data": 2},
        {"state": "EXECUTED", "date": "2023-01-01T12:00:00", "data": 1}
    ]),
    ("test_data_duplicates", True, [
        {"state": "EXECUTED", "date": "2023-01-01T12:00:00", "data": 1},
        {"state": "EXECUTED", "date": "2023-01-01T12:00:00", "data": 2},
        {"state": "CANCELED", "date": "2023-01-02T12:00:00", "data": 3},
        {"state": "CANCELED", "date": "2023-01-02T12:00:00", "data": 4}
    ]),
    ("test_data_empty", True, [])
])
def test_sort_by_date(fixture_name, sort_increase, expected, request):
    """Тесты сортировки по дате с использованием фикстур."""
    input_list = request.getfixturevalue(fixture_name)
    assert sort_by_date(input_list, sort_increase) == expected


def test_sort_by_date_invalid_format(test_data_invalid_dates):
    """Тест обработки некорректного формата даты."""
    with pytest.raises(ValueError):
        sort_by_date(test_data_invalid_dates)


def test_sort_by_date_empty(test_data_empty):
    """Тест обработки пустого списка."""
    assert sort_by_date(test_data_empty) == []
