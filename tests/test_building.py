import pytest
from models.building import Building
from models.apartment import Apartment


def test_building_init():
    bld = Building("Дом №1")

    assert bld.address == "Дом №1"
    assert bld.apartments == []


def test_building_add_apartment():
    bld = Building("Дом №2")
    apt = Apartment("ул. Ленина, 12", 3)

    bld.add_apartment(apt)

    assert len(bld.apartments) == 1
    assert bld.apartments[0].number == "ул. Ленина, 12"
    assert bld.apartments[0].residents == 3


def test_building_str():
    bld = Building("Дом №3")
    result = str(bld)

    assert "Дом №3" in result
