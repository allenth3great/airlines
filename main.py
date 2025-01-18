from add import add_flight
from book import book_ticket
from flight_data import flights
from view import view_flight_details  # Import the view function
from report import generate_flight_report  # Import the report function

def main():
    while True:
        print("\nWelcome to the Airline Management System!")
        print("\nWhat would you like to do?")
        print("1. Add")
        print("2. Book")
        print("3. View Flight Details")
        print("4. Generate Flight Report")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_flight()
            elif choice == 2:
                book_ticket()
            elif choice == 3:
                flight_number = int(input("Enter flight number: "))
                view_flight_details(flight_number)  # Call the view flight details function
            elif choice == 4:
                generate_flight_report()  # Call the report function
            elif choice == 5:
                print("Thank you for using the Airline Management System!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a numeric value for the choice.")    

# Run the program
if __name__ == "__main__":
    main()