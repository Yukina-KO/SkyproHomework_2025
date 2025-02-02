import os

import pytest

from src.decorators.decorators import log


def test_log_decorator_console_output(capsys: pytest.CaptureFixture) -> None:
    """Проверяем, что при отсутствии filename вывод идёт в консоль."""

    @log()
    def test_function(x: int, y: int) -> int:
        return x + y

    test_function(1, 2)
    captured = capsys.readouterr()
    output = captured.out
    assert "Начало выполнения функции test_function с аргументами: (1, 2), {}" in output
    assert "Функция test_function завершена. Результат: 3" in output


def test_log_decorator_file_output() -> None:
    """
    Проверяем, что при наличии файла декоратор пишет логи в файл, а не в консоль.
    Для этого указываем путь к test_log.txt в папке tests.
    """
    # Получаю абсолютный путь к "tests/test_log.txt"
    current_dir = os.path.dirname(__file__)  # Папка, где лежит test_decorators.py
    log_file = os.path.join(current_dir, "test_log.txt")

    # Если файла ещё нет в репозитории, можно создать пустой вручную
    if not os.path.exists(log_file):
        with open(log_file, "w", encoding="utf-8"):
            pass  # просто создаю пустой файл

    @log(filename=log_file)
    def test_function(x: int, y: int) -> int:
        return x + y

    # Вызываю декорированную функцию
    test_function(1, 2)

    # Проверяю, что теперь в файле есть логи
    assert os.path.exists(log_file), "Файл лога не создан!"
    with open(log_file, "r", encoding="utf-8") as f:
        log_content = f.read()
        assert "Начало выполнения функции test_function с аргументами: (1, 2), {}" in log_content
        assert "Функция test_function завершена. Результат: 3" in log_content


def test_log_decorator_error_handling(capsys: pytest.CaptureFixture) -> None:
    """Проверяю, что при возникновении ошибки декоратор логирует её."""

    @log()
    def test_function(x: int, y: int) -> None:
        raise ValueError("Test error")

    with pytest.raises(ValueError):
        test_function(1, 2)

    captured = capsys.readouterr()
    output = captured.out
    assert "Ошибка в функции test_function: ValueError - Test error. Аргументы: (1, 2), {}" in output


def test_log_decorator_argument_logging(capsys: pytest.CaptureFixture) -> None:
    """Проверяю корректное логирование позиционных и именованных аргументов."""

    @log()
    def test_function(x: int, y: int) -> int:
        return x + y

    test_function(1, y=2)
    captured = capsys.readouterr()
    output = captured.out
    assert "Начало выполнения функции test_function с аргументами: (1,), {'y': 2}" in output


def test_log_decorator_metadata_preservation() -> None:
    """Проверяю, что декоратор сохраняет __name__ и __doc__ функции."""

    @log()
    def test_function(x: int, y: int) -> int:
        """Test function documentation."""
        return x + y

    assert test_function.__name__ == "test_function"
    assert test_function.__doc__ == "Test function documentation."
