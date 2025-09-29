import pytest
from models.management_company import ManagementCompany
from models.apartment import Apartment


def test_management_company_init():
    mc = ManagementCompany("ул. Ленина, 10", "ООО Управдом", "1234567890")

    assert mc.address == "ул. Ленина, 10"
    assert mc.company_name == "ООО Управдом"
    assert mc.inn == "1234567890"
    assert mc.apartments == []


def test_management_company_get_path_to_counters():
    mc = ManagementCompany("ул. Гагарина 15", "ТСЖ Согласие", "9876543210")

    path = mc.get_path_to_counters()
    assert path == "./ул.Гагарина15"


def test_management_company_add_apartment():
    mc = ManagementCompany("ул. Кирова, 5", "ЖК Уютный", "555666777")
    apt = Apartment("Квартира 12", 4)

    mc.add_apartment(apt)

    assert len(mc.apartments) == 1
    assert mc.apartments[0].number == "Квартира 12"
    assert mc.apartments[0].residents == 4


def test_management_company_str():
    mc = ManagementCompany("ул. Победы, 7", "ДомСервис", "111222333")
    result = str(mc)

    assert "Управляющая компания: ДомСервис" in result
    assert "ИНН: 111222333" in result
    assert "ул. Победы, 7" in result
