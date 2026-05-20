def check_even_odd(n):
    return "even" if n % 2 == 0 else "odd"


if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
    else:
        print(f"{number} is {check_even_odd(number)}")
