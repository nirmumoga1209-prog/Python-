books = []


def add_book(title):
    if title in books:
        print(f"\n'{title}' is already in the library.")
        return
    books.append(title)
    print(f"\n'{title}' added.")


def remove_book(title):
    if title in books:
        books.remove(title)
        print(f"\n'{title}' removed.")
    else:
        print(f"\n'{title}' not found.")


def search_book(title):
    if title in books:
        print(f"\n'{title}' is available.")
    else:
        print(f"\n'{title}' is not available.")


def display_books():
    if not books:
        print("\nNo books in the library.")
        return
    print("\nLibrary books:")
    for idx, title in enumerate(books, start=1):
        print(f"{idx}. {title}")


def show_menu():
    print("\nLibrary Book System")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Book")
    print("4. Display Books")
    print("5. Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            title = input("Enter book title to add: ").strip()
            add_book(title)
        elif choice == "2":
            title = input("Enter book title to remove: ").strip()
            remove_book(title)
        elif choice == "3":
            title = input("Enter book title to search: ").strip()
            search_book(title)
        elif choice == "4":
            display_books()
        elif choice == "5":
            print("Exiting library system.")
            break
        else:
            print("Invalid choice. Please enter 1-5.")


if __name__ == "__main__":
    main()
