contacts = {}


def add_contact(name, phone):
    if name in contacts:
        print(f"\nContact '{name}' already exists.")
        return
    contacts[name] = phone
    print(f"\nContact '{name}' added.")


def search_contact(name):
    if name in contacts:
        print(f"\n{name}: {contacts[name]}")
    else:
        print(f"\nContact '{name}' not found.")


def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"\nContact '{name}' deleted.")
    else:
        print(f"\nContact '{name}' not found.")


def display_contacts():
    if not contacts:
        print("\nNo contacts available.")
        return
    print("\nContacts:")
    for name, phone in contacts.items():
        print(f"{name}: {phone}")


def show_menu():
    print("\nContact Book")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Display Contacts")
    print("5. Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            name = input("Enter name: ").strip()
            phone = input("Enter phone number: ").strip()
            add_contact(name, phone)
        elif choice == "2":
            name = input("Enter name to search: ").strip()
            search_contact(name)
        elif choice == "3":
            name = input("Enter name to delete: ").strip()
            delete_contact(name)
        elif choice == "4":
            display_contacts()
        elif choice == "5":
            print("Exiting contact book.")
            break
        else:
            print("Invalid choice. Please enter 1-5.")


if __name__ == "__main__":
    main()
