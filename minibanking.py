balance = 0.0


def deposit(amount):
    global balance
    if amount <= 0:
        print("Deposit amount must be positive.")
        return False
    balance += amount
    print(f"Deposited {amount}. Current balance: {balance}")
    return True


def withdraw(amount):
    global balance
    if amount <= 0:
        print("Withdrawal amount must be positive.")
        return False
    if amount > balance:
        print("Insufficient funds.")
        return False
    balance -= amount
    print(f"Withdrew {amount}. Current balance: {balance}")
    return True


def check_balance():
    print(f"Current balance: {balance}")
    return balance


if __name__ == "__main__":
    while True:
        print("\nMini Banking System")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            try:
                amount = float(input("Enter deposit amount: "))
            except ValueError:
                print("Invalid amount.")
            else:
                deposit(amount)
        elif choice == "2":
            try:
                amount = float(input("Enter withdrawal amount: "))
            except ValueError:
                print("Invalid amount.")
            else:
                withdraw(amount)
        elif choice == "3":
            check_balance()
        elif choice == "4":
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please select 1-4.")
