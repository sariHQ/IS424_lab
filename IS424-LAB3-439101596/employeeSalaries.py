


employeesDict = {}

while True:
    name = input("--------------------\n"
                 "*note* to end write (no).\n"
                 "\nPlease enter the employee name: ")

    if name == 'no':
        break

    salary = input("Please enter the employee salary: ")
    employeesDict[name] = float(salary)

print("--------------------\nEmployee name and salary\n")
for name, salary in employeesDict.items():
    print(f"{name}: {salary}")



