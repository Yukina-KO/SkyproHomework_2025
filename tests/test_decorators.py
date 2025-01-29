import pytest
from typing import Any
from src.decorators.decorators import log


# Тестирование вывода в консоль
def test_log_decorator_console_output(capsys: pytest.CaptureFixture) -> None:
    @log()
    def test_function(x: int, y: int) -> int:
        return x + y

    test_function(1, 2)

    captured = capsys.readouterr()
    output = captured.out
    assert "Начало выполнения функции test_function с аргументами: (1, 2), {}" in output
    assert "Функция test_function завершена. Результат: 3" in output


# Тестирование записи в файл
def test_log_decorator_file_output(tmpdir: Any) -> None:
    log_file = tmpdir.join("test_log.txt")

    @log(filename=str(log_file))
    def test_function(x: int, y: int) -> int:
        return x + y

    test_function(1, 2)

    assert log_file.exists()
    with open(log_file, "r", encoding="utf-8") as f:
        log_content = f.read()
        assert "Начало выполнения функции test_function с аргументами: (1, 2), {}" in log_content
        assert "Функция test_function завершена. Результат: 3" in log_content


# Тестирование обработки ошибок
def test_log_decorator_error_handling(capsys: pytest.CaptureFixture) -> None:
    @log()
    def test_function(x: int, y: int) -> None:
        raise ValueError("Test error")

    with pytest.raises(ValueError):
        test_function(1, 2)

    captured = capsys.readouterr()
    output = captured.out
    assert "Ошибка в функции test_function: ValueError - Test error. Аргументы: (1, 2), {}" in output


# Тестирование логирования аргументов
def test_log_decorator_argument_logging(capsys: pytest.CaptureFixture) -> None:
    @log()
    def test_function(x: int, y: int) -> int:
        return x + y

    test_function(1, y=2)

    captured = capsys.readouterr()
    output = captured.out
    assert "Начало выполнения функции test_function с аргументами: (1,), {'y': 2}" in output


# Тестирование сохранения метаданных функции
def test_log_decorator_metadata_preservation() -> None:
    @log()
    def test_function(x: int, y: int) -> int:
        """Test function documentation."""
        return x + y

    assert test_function.__name__ == "test_function"
    assert test_function.__doc__ == "Test function documentation."
