import pytest
import json
from unittest.mock import mock_open, patch
from services.data_loader import (
    load_building_data,
    read_residents_count,
    read_counters_data,
    get_counters_file_path,
    add_counters_to_apartment,
)
from models.management_company import ManagementCompany
from models.apartment import Apartment
from models.showing_counter import ShowingCounter


def test_load_building_data():
    fake_json = [
        {"address": "ул. Пушкина, 10", "company_name": "УК Тест", "inn": "111", "apartments": ["1"]}
    ]
    m = mock_open(read_data=json.dumps(fake_json, ensure_ascii=False))

    with patch("builtins.open", m):
        result = load_building_data()

    assert result[0]["address"] == "ул. Пушкина, 10"
    assert result[0]["company_name"] == "УК Тест"


def test_read_residents_count():
    mc = ManagementCompany("ул. Пушкина, 10", "УК Тест", "111")
    file_data = "5\n"
    m = mock_open(read_data=file_data)

    with patch("builtins.open", m):
        residents = read_residents_count(mc, "1")

    assert residents == 5


def test_read_counters_data_with_mock():
    mc = ManagementCompany("ул. Пушкина, 10", "УК Тест", "111")
    file_data = (
        "3\n"
        '"Вода" 2025.09.29 100\n'
        '"Электричество" 2025.09.29 200\n'
    )
    m = mock_open(read_data=file_data)

    with patch("builtins.open", m):
        counters = read_counters_data(mc, "1")

    assert counters == [
        ('"Вода"', "2025.09.29", 100),
        ('"Электричество"', "2025.09.29", 200),
    ]


def test_add_counters_to_apartment_creates_showing_counters():
    apt = Apartment("1", 2)
    counters_data = [('"Вода"', "2025.09.29", 123)]

    add_counters_to_apartment(apt, counters_data)

    assert len(apt.counters) == 1
    assert isinstance(apt.counters[0], ShowingCounter)
    assert apt.counters[0].count == 123
