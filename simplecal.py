def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b if b != 0 else None


if __name__ == "__main__":
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
    else:
        print("Addition:", add(num1, num2))
        print("Subtraction:", subtract(num1, num2))
        print("Multiplication:", multiply(num1, num2))
        if num2 == 0:
            print("Division: Cannot divide by zero")
        else:
            print("Division:", divide(num1, num2))
