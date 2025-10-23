from lab0202_employee import Employee

class Salesperson(Employee):
    
    def __init__(self, id: int, name: str, department: str, base_salary: float, 
                 commission_rate: float, sales_volume: float):
        super().__init__(id, name, department, base_salary)
        self.commission_rate = commission_rate
        self.sales_volume = sales_volume
    
    @property
    def commission_rate(self):
        return self.__commission_rate
    
    @commission_rate.setter
    def commission_rate(self, value):
        if not isinstance(value, (int, float)) or value < 0 or value > 1:
            raise ValueError("Процент комиссии должен быть вещественным числом от 0 до 1 включительно.")
        self.__commission_rate = float(value)
    
    @property
    def sales_volume(self):
        return self.__sales_volume
    
    @sales_volume.setter
    def sales_volume(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Объем продаж должен быть неотрицательным числом.")
        self.__sales_volume = float(value)
    
    def update_sales(self, amount: float) -> None:
        if not isinstance(amount, (int, float)):
            raise ValueError("Изменение объёма продаж должно быть числом.")
        new_volume = self.sales_volume + amount
        if new_volume < 0:
            raise ValueError(f"Объём продаж не может быть отрицательным. Текущий: {self.sales_volume}, изменение: {amount}")
        self.sales_volume = new_volume
        
    def calculate_salary(self) -> float:
        """Расчет зарплаты: базовая + комиссия от объема продаж."""
        return self.base_salary + (self.sales_volume * self.commission_rate)
    
    def get_info(self) -> str:
        """Полная информация о продавце."""
        return (f"Продавец [id: {self.id}, имя: {self.name}, отдел: {self.department}, "
                f"базовая зарплата: {self.base_salary:.2f}, процент комиссии: {self.commission_rate:.1%}, "
                f"объём продаж: {self.sales_volume:.2f}, итоговая зарплата: {self.calculate_salary():.2f}]")