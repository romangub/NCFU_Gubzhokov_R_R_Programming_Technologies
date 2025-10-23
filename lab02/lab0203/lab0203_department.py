from lab0202_abstract_employee import AbstractEmployee
from typing import Optional

class Department:
    
    def __init__(self, name: str):
        self.name = name
        self.emp_list = []
        
    def add_employee(self, employee: AbstractEmployee):
        if employee.id not in [emp.id for emp in self.emp_list]:
            employee.department = self.name
            self.emp_list.append(employee)
        else:
            raise ValueError(f'Сотрудник {employee.name} id = {employee.id} уже находится в департаменте "{self.name}"')
            
    def remove_employee(self, employee_id: int) -> None:
        initial_count = len(self.emp_list)
        self.emp_list = [emp for emp in self.emp_list if emp.id != employee_id]
        
        if len(self.emp_list) == initial_count:
            raise ValueError(f'В департаменте "{self.name}" нет id = {employee_id}')
    
    def get_employees(self) -> list[AbstractEmployee]:
        return [{"Name": emp.name, "ID": emp.id, "Department": emp.department, "Base Salary": emp.base_salary} for emp in self.emp_list]
    
    def calculate_total_salary(self) -> float:
        return sum([emp.calculate_salary() for emp in self.emp_list])
    
    def get_employee_count(self) -> dict[str, int]:
        count_dict = {}
        for emp in self.emp_list:
            emp_type = emp.__class__.__name__
            count_dict[emp_type] = count_dict.get(emp_type, 0) + 1
        return count_dict
    
    def find_employee_by_id(self, employee_id: int) -> Optional[AbstractEmployee]:
        for emp in self.emp_list:
            if emp.id == employee_id:
                return emp
        return None

from lab0202_employee import Employee
from lab0202_manager import Manager
from lab0202_developer import Developer
from lab0202_salesperson import Salesperson

employee1 = Employee(id=100, name="Иван Иванов", department="", base_salary=50000)
employee2 = Employee(id=101, name="Диван Иванов", department="", base_salary=55000)
employee3 = Developer(id=102, name="Ливан Иванов", department="", base_salary=60000, 
                     tech_stack=["Python", "Java"], seniority_level="middle")
employee4 = Manager(id=103, name="Ниван Иванов", department="", base_salary=70000, bonus=15000)
employee5 = Salesperson(id=104, name="Ван Иванов", department="", base_salary=40000, 
                       commission_rate=0.1, sales_volume=500000)

department = Department("Отдельный отдел")

department.add_employee(employee1)
department.add_employee(employee2)
department.add_employee(employee3)
department.add_employee(employee4)
department.add_employee(employee5)

print(department.calculate_total_salary())