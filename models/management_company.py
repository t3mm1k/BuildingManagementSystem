from .building import Building


class ManagementCompany(Building):
    def __init__(self, address: str, company_name: str, inn: str) -> None:
        super().__init__(address)
        self.company_name = company_name
        self.inn = inn

    def get_path_to_counters(self) -> str:
        return f"./{self.address.replace(' ', '')}"

    def __str__(self) -> str:
        base_info = super().__str__()
        return (
            f'Управляющая компания: {self.company_name}\n'
            f'ИНН: {self.inn}\n'
            f'{base_info}'
        )