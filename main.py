from services.data_loader import load_building_data, create_management_companies
from models.building import Building


def display_building_info(buildings: list[Building]) -> None:
    for building in buildings:
        print(building)


def create_sample_data():
    building_data = load_building_data()
    return create_management_companies(building_data)


if __name__ == '__main__':
    managements_company = create_sample_data()
    display_building_info(managements_company)