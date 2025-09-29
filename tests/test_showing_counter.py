import pytest
from datetime import date
from models.showing_counter import ShowingCounter


def test_showing_counter_init():
    counter = ShowingCounter("Электричество", "2025.09.29", 123)

    assert counter.type == "Электричество"
    assert counter.date == date(2025, 9, 29)
    assert counter.count == 123


def test_showing_counter_str():
    counter = ShowingCounter("Вода", "2023.01.15", 45)
    result = str(counter)

    assert "Тип ресурса: Вода" in result
    assert "Дата: 2023-01-15" in result  # date преобразуется в ISO формат
    assert "Показатель: 45" in result


def test_showing_counter_invalid_date():
    with pytest.raises(ValueError):
        ShowingCounter("Газ", "15-01-2023", 10)  # неверный формат даты
