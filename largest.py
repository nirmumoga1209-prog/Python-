def largest_of_three(a, b, c):
    return max(a, b, c)


if __name__ == "__main__":
    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        z = float(input("Enter third number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
    else:
        print("Largest number:", largest_of_three(x, y, z))
