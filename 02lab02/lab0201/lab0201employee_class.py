class Employee:
    def __init__(self, id: int, name: str, department: str, base_salary: float):
        self.id = id 
        self.name = name
        self.department = department 
        self.base_salary = base_salary 
    
    def __str__(self):
        return f"Сотрудник [id: {self.id}, имя: {self.name}, отдел: {self.department}, базовая зарплата: {self.base_salary}]"
        
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("ID должен быть положительным целым числом.")
        self.__id = value
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or value.strip() == "":
            raise ValueError("Имя не может быть пустой строкой.")
        self.__name = value
        
    @property
    def department(self):
        return self.__department
    
    @department.setter
    def department(self, value):
        if not isinstance(value, str):
            raise ValueError("Название отдела должно быть строкой.")
        self.__department = value
    
    @property
    def base_salary(self):
        return self.__base_salary
    
    @base_salary.setter
    def base_salary(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Зарплата должна быть неотрицательным числом.")
        self.__base_salary = value