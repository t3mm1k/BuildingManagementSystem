import json
import re
from typing import List, Tuple
from models.management_company import ManagementCompany
from models.apartment import Apartment
from models.showing_counter import ShowingCounter


def load_building_data() -> List[dict]:
    with open('./building.json', 'r', encoding='utf-8') as f:
        return json.load(f)


def create_management_companies(building_data: List[dict]) -> List[ManagementCompany]:
    management_companies = []

    for building_info in building_data:
        management_company = create_management_company(building_info)
        management_companies.append(management_company)

    return management_companies


def create_management_company(building_info: dict) -> ManagementCompany:
    management_company = ManagementCompany(
        address=building_info['address'],
        company_name=building_info['company_name'],
        inn=building_info['inn']
    )

    for apartment_number in building_info['apartments']:
        apartment = create_apartment_with_counters(management_company, apartment_number)
        management_company.add_apartment(apartment)

    return management_company


def create_apartment_with_counters(management_company: ManagementCompany,
                                   apartment_number: str) -> Apartment:
    residents = read_residents_count(management_company, apartment_number)
    apartment = Apartment(apartment_number, residents)

    counters_data = read_counters_data(management_company, apartment_number)
    add_counters_to_apartment(apartment, counters_data)

    return apartment


def read_residents_count(management_company: ManagementCompany,
                         apartment_number: str) -> int:
    file_path = get_counters_file_path(management_company, apartment_number)

    with open(file_path, 'r', encoding='utf-8') as f:
        return int(f.readline().strip())


def read_counters_data(management_company: ManagementCompany,
                       apartment_number: str) -> List[Tuple[str, str, int]]:
    file_path = get_counters_file_path(management_company, apartment_number)
    counters_data = []

    with open(file_path, 'r', encoding='utf-8') as f:
        f.readline()

        for line in f:
            type = re.search(r'"[а-яА-Я]+"', line).group()
            date = re.search(r'\d\d\d\d.\d\d.\d\d', line).group()
            count = re.search(r'(?<!\d\.)\b\d+\b(?!\.\d)', line).group()
            counters_data.append((type, date, int(count)))

    return counters_data


def get_counters_file_path(management_company: ManagementCompany,
                           apartment_number: str) -> str:
    base_path = management_company.get_path_to_counters()
    return f"{base_path}_{apartment_number}.txt"


def add_counters_to_apartment(apartment: Apartment,
                              counters_data: List[Tuple[str, str, int]]) -> None:
    for type, date, count in counters_data:
        counter = ShowingCounter(type, date, count)
        apartment.add_counter(counter)