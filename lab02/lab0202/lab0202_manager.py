from lab0202_employee import Employee

class Manager(Employee):
    
    def __init__(self, id: int,
                 name: str,
                 department: str,
                 base_salary: float,
                 bonus: float):
        super().__init__(id, name, department, base_salary)
        self.bonus = bonus
    
    @property
    def bonus(self):
        return self.__bonus
    
    @bonus.setter
    def bonus(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Бонус должен быть неотрицательным числом.")
        self.__bonus = float(value)
    
    def get_info(self) -> str:
        return (f"Менеджер [id: {self.id}, имя: {self.name}, отдел: {self.department}, базовая зарплата: {self.base_salary}, бонус: {self.bonus}, итоговая зарплата: {self.calculate_salary()}]")
    
    def calculate_salary(self):
        return self.base_salary + self.bonus