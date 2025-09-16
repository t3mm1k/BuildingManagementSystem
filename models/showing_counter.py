from datetime import datetime


class ShowingCounter:
    def __init__(self, type: str, date: str, count: int) -> None:
        self.type = type
        self.date = datetime.strptime(date, '%Y.%m.%d').date()
        self.count = count

    def __str__(self) -> str:
        return (
            f'Тип ресурса: {self.type}\n'
            f'Дата: {self.date}\n'
            f'Показатель: {self.count}'
        )