employees = {}


def add_employee(name, salary):
	if name in employees:
		return False
	employees[name] = salary
	return True


def update_salary(name, salary):
	if name not in employees:
		return False
	employees[name] = salary
	return True


def search_employee(name):
	return employees.get(name)


if __name__ == "__main__":
	# demo usage
	add_employee("Rina", 50000)
	add_employee("Sahil", 62000)
	print("Employees after adding:", employees)

	updated = update_salary("Rina", 55000)
	print("Updated Rina salary:", updated)
	print("Employees after update:", employees)

	print("Search Sahil:", search_employee("Sahil"))
	print("Search Unknown:", search_employee("Unknown"))

