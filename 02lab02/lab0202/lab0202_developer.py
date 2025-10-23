from lab0202_employee import Employee

class Developer(Employee):
    
    def __init__(self,
                 id: int,
                 name: str,
                 department: str,
                 base_salary: float, 
                 tech_stack: list[str],
                 seniority_level: str):
        super().__init__(id, name, department, base_salary)
        self.tech_stack = tech_stack
        self.seniority_level = seniority_level
        
    @property
    def tech_stack(self):
        return self.__tech_stack
        
    @tech_stack.setter
    def tech_stack(self, value):
        if not isinstance(value, list) or len(value) == 0:
            raise ValueError("Компетенции должны быть непустым списком")
        if not all(isinstance(item, str) for item in value):
            raise ValueError("Все элементы tech_stack должны быть строками")
        self.__tech_stack = value
            
    @property
    def seniority_level(self):
        return self.__seniority_level
        
    @seniority_level.setter
    def seniority_level(self, value):
        valid_levels = ["junior", "middle", "senior"]
        if value.lower() not in valid_levels:
            raise ValueError(f'Уровень разработчика должен быть одним из: "junior", "middle", "senior"')
        self.__seniority_level = value.lower()
    
    @property
    def seniority_coefficient(self):
        table = {"junior": 1.0, "middle": 1.5, "senior": 2.0}
        return table[self.seniority_level]
    
    def add_skill(self, new_skill: str) -> None:
        if not isinstance(new_skill, str) or new_skill.strip() == "":
            raise ValueError("Технология должна быть непустой строкой")
        if new_skill not in self.tech_stack:
            self.tech_stack.append(new_skill)
    
    def calculate_salary(self) -> float:
        return self.base_salary * self.seniority_coefficient
    
    def get_info(self) -> str:
        return (f"Разработчик [id: {self.id}, имя: {self.name}, отдел: {self.department}, "
                f"базовая зарплата: {self.base_salary}, компетенции: {', '.join(self.tech_stack)}, "
                f"уровень: {self.seniority_level}, итоговая зарплата: {self.calculate_salary():.2f}]")