salary = float(input("Enter salary: "))
years = float(input("Enter years of service: "))

if years >= 5:
    bonus = salary * 0.10
    total_salary = salary + bonus
    print("Bonus awarded: ", bonus)
    print("New Salary: ", total_salary)
else:
    print("No bonus awarded.")
    