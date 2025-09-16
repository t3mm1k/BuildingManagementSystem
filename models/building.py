from typing import List
from .apartment import Apartment


class Building:
    def __init__(self, address: str) -> None:
        self.address = address
        self.apartments: List[Apartment] = []

    def add_apartment(self, apartment: Apartment) -> None:
        self.apartments.append(apartment)

    def get_apartments_count(self) -> int:
        return len(self.apartments)

    def __str__(self) -> str:
        result = f'Адрес здания: {self.address}\n'
        result += f'Количество квартир: {self.get_apartments_count()}\n\n'

        for i, apartment in enumerate(self.apartments, 1):
            result += str(apartment) + '\n'

        return result