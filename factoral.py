def factorial(n):
	if n < 0:
		return None
	result = 1
	for i in range(2, n + 1):
		result *= i
	return result


if __name__ == "__main__":
	try:
		num = int(input("Enter a non-negative integer: "))
	except ValueError:
		print("Invalid input. Please enter an integer.")
	else:
		res = factorial(num)
		if res is None:
			print("Factorial not defined for negative numbers.")
		else:
			print(f"Factorial of {num} is {res}")

			