from lab0202_abstract_employee import AbstractEmployee

class Employee(AbstractEmployee):
    def __init__(self, id: int, name: str, department: str, base_salary: float):
        super().__init__(id, name, department, base_salary)

    def calculate_salary(self) -> float:
        return self.base_salary

    def get_info(self) -> str:
        return f"Сотрудник [id: {self.id}, имя: {self.name}, отдел: {self.department}, базовая зарплата: {self.base_salary}]"

    def __str__(self):
        return self.get_info()