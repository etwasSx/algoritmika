# example programm for students of "Algoritmika"
# data_storage_system_september.py

# Система для хранения данных
employees = {
    "Иванов" : {
        "должность" : "руководитель проектов",
        "коэфициент эффективности" : 71.3,
        "проекты" : ["Арканоид", "Memory Cards", "Fast Clicker"],
        "зарплата": 120000
    },
    "Петров" : {
        "должность" : "старший программист",
        "коэфициент эффективности" : 65.1,
        "проекты" : ["Арканоид", "Memory Cards", "Fast Clicker", "Индекс массы тела"],
        "зарплата": 85000
    },
    "Сидоров" : {
        "должность" : "дизайнер",
        "коэфициент эффективности" : 60.4,
        "проекты" : ["Арканоид", "Memory Cards", "Fast Clicker"],
        "зарплата": 68000
    }
}

# Программное добавление элемента. функция принимает параметры 
# (фамилия, должность, коэфициент эффективности, проекты, зарплата)
# можно делать без функции. Вместо перменных подставлять значения
def add_new_employee(name, post, ec, projects, salary):
    employees[name] = {
        "должность" : post,
        "коэфициент эффективности" : ec,
        "проекты" : projects,
        "зарплата": salary
    }

add_new_employee("Васильев", "младший программист", 33.1,  ["Memory Cards", "Fast Clicker"], 45000)

add_new_employee("Григорьев", "младший программист", 45.1,  ["Memory Cards"], 53000)

add_new_employee("Рыскин", "старший программист", 86.8, ["Арканоид", "Memory Cards", "Fast Clicker", "Индекс массы тела"], 105000)

# Вывод всех фамилий
index = 1
print("Фамилии работников:")

# Перебор словаря по его ключам (фамилиям)
for employee in employees.keys():
    print(index,"-", employee)
    index += 1

print("------------------")
# Вывод самого эффективного сотрудника
max_ec = 0
name = ""
# Алгоритм нахождение максимума
for employee in employees:
    if employees[employee]["коэфициент эффективности"] > max_ec:
        name = employee
        max_ec = employees[employee]["коэфициент эффективности"]

print("Максимальная эффективность:")
print(name, "-", max_ec)

# Вывод всех должностей и фамилий работников
print("------------------")
index = 1 # для создания нумерации
for employee in employees:
    print(str(index) + ")", employee, "-", employees[employee]["должность"])
    index += 1
