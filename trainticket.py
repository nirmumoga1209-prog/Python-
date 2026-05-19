# Train Seat Reservation System

# Initialize 20 seats, 0 = available, 1 = booked
seats = [0] * 20

def display_menu():
    print("\n1. Book Seat")
    print("2. Cancel Seat")
    print("3. Show Seats")
    print("4. Booking Percentage")
    print("5. Exit")

def book_seat():
    try:
        seat_num = int(input("Enter seat number (1-20): "))
        if 1 <= seat_num <= 20:
            if seats[seat_num - 1] == 0:
                seats[seat_num - 1] = 1
                print(f"Seat {seat_num} booked successfully.")
            else:
                print(f"Seat {seat_num} is already booked.")
        else:
            print("Invalid seat number. Please enter 1-20.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def cancel_seat():
    try:
        seat_num = int(input("Enter seat number (1-20): "))
        if 1 <= seat_num <= 20:
            if seats[seat_num - 1] == 1:
                seats[seat_num - 1] = 0
                print(f"Seat {seat_num} cancelled successfully.")
            else:
                print(f"Seat {seat_num} is already available.")
        else:
            print("Invalid seat number. Please enter 1-20.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def show_seats():
    print("Seat Status (0=Available, 1=Booked):")
    for i in range(20):
        print(f"Seat {i+1}: {seats[i]}", end=" ")
        if (i+1) % 5 == 0:
            print()
    print()

def booking_percentage():
    booked = sum(seats)
    percentage = (booked / 20) * 100
    print(f"Booking Percentage: {percentage:.2f}%")

def main():
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                book_seat()
            elif choice == 2:
                cancel_seat()
            elif choice == 3:
                show_seats()
            elif choice == 4:
                booking_percentage()
            elif choice == 5:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter 1-5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main() 
      