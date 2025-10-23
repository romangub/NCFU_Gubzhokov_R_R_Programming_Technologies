from lab0201employee_class import Employee

if __name__ == "__main__":
    emp = Employee(165, "Shipazu", "Отдел Дизайна", 0)
    print(emp.id)
    print(emp.name)
    print(emp.department)
    print(emp.base_salary)
    
    emp.department = "Графический Отдел"
    print(emp.department)
    
    try:
        emp.base_salary = -100500
    except ValueError as e:
        print(f"Error: {e}")
        
    emp.base_salary = 65.050
    print(emp.base_salary)
    
    print(emp)