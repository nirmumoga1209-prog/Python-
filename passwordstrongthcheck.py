def is_strong_password(password):
    if len(password) < 8:
        return False
    has_digit = any(ch.isdigit() for ch in password)
    has_upper = any(ch.isupper() for ch in password)
    has_lower = any(ch.islower() for ch in password)
    return has_digit and has_upper and has_lower


if __name__ == "__main__":
    pwd = input("Enter password to check: ")
    if is_strong_password(pwd):
        print("Password is strong")
    else:
        print("Password is weak")
