datos = [
    {"nombre": "Ana", "depto": "IT", "salario": 50000},
    {"nombre": "Bob", "depto": "HR", "salario": 45000},
    {"nombre": "Carlos", "depto": "IT", "salario": 55000},
]

def get_by_name_and_salary(employees):
    return [{"nombre": employee["nombre"], "salario": employee["salario"]} for employee in employees]

def filter_by_min_earning(employees, min_earning):
    return [employee for employee in employees if employee["salario"] > min_earning]

def group_by_department(employees):
    deptos = set(e["depto"] for e in employees)
    return {
        depto: [e for e in employees if e["depto"] == depto]
        for depto in deptos
    }

def calculate_avg_salaries(employees):
    return sum(employee["salario"] for employee in employees) / len(employees)
    
def main():
    print(get_by_name_and_salary(datos))
    print(filter_by_min_earning(datos, 48000))
    print(group_by_department(datos))
    print(calculate_avg_salaries(datos))
    pass



if __name__ == "__main__":
    main()