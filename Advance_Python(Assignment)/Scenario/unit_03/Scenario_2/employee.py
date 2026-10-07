import csv
import os

folder = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(folder, "employee.csv")

with open(file_path, "r", newline="") as file:
    employees = list(csv.DictReader(file))

print("Employee Details")
print("-" * 40)

for employee in employees:
    print(employee)

print("-" * 40)

emp_id = input("Enter Employee ID to search: ")

found = False

for employee in employees:
    if employee["Employee ID"] == emp_id:
        print("\nEmployee Found:")
        print("Employee ID:", employee["Employee ID"])
        print("Name:", employee["Name"])
        print("Department:", employee["Department"])
        print("Salary:", employee["Salary"])
        found = True
        break

if not found:
    print("Employee not found.")