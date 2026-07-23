def cleaned_city(city):
  return city.strip().title()
def cleaned_name(name):
  return name.strip().title()
import json # Added missing import for json
with open("employees.json","w") as file:
  json.dump(employees, file, indent=4)
with open("employees.json","r") as file:
  employees=json.load(file)
  total_employees=0
  valid_employees=0
  total_salary=0
  avg_salary=0
  highest_salary=0
  highest_paid=""
  employee_count_by_city={}
  for emp in employees:
    total_employees+=1
    if emp.get("salary",0)>0:
      valid_employees+=1
      # Accumulate total_salary correctly
      total_salary+=emp["salary"]
      if emp["salary"]>highest_salary:
        highest_salary=emp["salary"]
        highest_paid=cleaned_name(emp["name"])
    city=cleaned_city(emp["city"])
    if city not in employee_count_by_city:
      employee_count_by_city[city]=0
    employee_count_by_city[city]+=1
  print(f"total employees: {total_employees}")
  print(f"Total salary: {total_salary}")
  # Check for division by zero
  print(f"Average salary: {total_salary/valid_employees if valid_employees > 0 else 0}")
  print(f"Highest-paid employee: {highest_paid}")
  print("Employee count by city:")
  print(employee_count_by_city)

# Separate writing and reading operations for clean_employees.json
cleaned_employees_list = []
for emp in employees:
    # Create a copy to avoid modifying the original 'employees' list while iterating if it's used elsewhere
    # However, in this specific code, the 'employees' list is immediately overwritten after this block,
    # so direct modification is fine. For general robustness, copying is often safer.
    cleaned_emp = emp.copy() # Using .copy() to ensure we don't modify the original list reference if it were needed later.
    cleaned_emp["name"] = cleaned_name(cleaned_emp["name"])
    cleaned_emp["city"] = cleaned_city(cleaned_emp["city"])
    cleaned_employees_list.append(cleaned_emp)

with open("clean_employees.json","w") as file:
  json.dump(cleaned_employees_list, file, indent=4)

with open("clean_employees.json","r") as outfile:
  employees=json.load(outfile)
  for emp in employees:
    print(emp)
