from add import add_flight
from book import book_ticket
from flight_data import flights
from view import view_flight_details  
from report import generate_flight_report  

def main():
    print("Welcome to the Airlines Management System!\n")
    
    while True:
        action = input("What would you like to do? (add/book/view/report/exit): ").strip().lower()
        
        if action == "add":
            add_flight()
        elif action == "book":
            book_ticket()
        elif action == "view":
            try:
                flight_number = int(input("Enter flight number: "))
                view_flight_details(flight_number)  
            except ValueError:
                print("Invalid input. Please enter a numeric value for the flight number.")
        elif action == "report":
            generate_flight_report()  
        elif action == "exit":
            print("Thank you for using the Airlines Management System!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the program
if __name__ == "__main__":
    main()
