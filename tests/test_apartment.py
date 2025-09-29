import pytest
from models.apartment import Apartment
from models.showing_counter import ShowingCounter


def test_apartment_init():
    apt = Apartment("ул. Ленина, 10", 3)

    assert apt.number == "ул. Ленина, 10"
    assert apt.residents == 3
    assert apt.counters == []


def test_apartment_add_counter():
    apt = Apartment("ул. Гагарина, 5", 2)
    counter = ShowingCounter("Электричество", "2025.09.29", 150)

    apt.add_counter(counter)

    assert len(apt.counters) == 1
    assert apt.counters[0].type == "Электричество"
    assert apt.counters[0].count == 150


def test_apartment_str():
    apt = Apartment("ул. Кирова, 7", 4)
    result = str(apt)

    assert "ул. Кирова, 7" in result
    assert "4" in result
