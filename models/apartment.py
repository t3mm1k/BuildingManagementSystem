from typing import List

from .showing_counter import ShowingCounter


class Apartment:
    def __init__(self, address: str, residents: int) -> None:
        self.number = address
        self.residents = residents
        self.counters: List[ShowingCounter] = []

    def add_counter(self, counter: ShowingCounter) -> None:
        self.counters.append(counter)

    def __str__(self) -> str:
        counter_string = '\n'.join(str(counter) for counter in self.counters)
        return (
            f'Квартира №{self.number}\n'
            f'Кол-во проживающих: {self.residents}\n'
            f'Счетчики: \n{counter_string}\n'
        )