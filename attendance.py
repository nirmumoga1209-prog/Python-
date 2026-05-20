students = []


def add_student(name):
	if name in students:
		return False
	students.append(name)
	return True


def remove_student(name):
	try:
		students.remove(name)
		return True
	except ValueError:
		return False


def display_students():
	if not students:
		print("No students enrolled.")
		return
	for i, name in enumerate(students, start=1):
		print(f"{i}. {name}")


if __name__ == "__main__":
	# sample usage
	add_student("Aarav")
	add_student("Bhavya")
	add_student("Chirag")
	print("After adding:")
	display_students()
	print()
	remove_student("Bhavya")
	print("After removing Bhavya:")
	display_students()