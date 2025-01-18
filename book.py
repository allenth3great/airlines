from flight_data import flights

def book_ticket():
    try:
        flight_num = int(input("Enter flight number: "))
        
        # Check if the flight exists
        if flight_num not in flights:
            print("Flight not found.")
            return
        
        flight_info = flights[flight_num]
        seat_capacity = flight_info["Seat Capacity"]
        
        booked_seats = flight_info.get("Booked Seats", {})

        # Check for available seats
        available_seats = [seat for seat in range(1, seat_capacity + 1) if seat not in booked_seats]
        
        if not available_seats:
            print("No available seats on this flight.")
            return
        
        passenger_name = input("Enter passenger name: ")
        seat_number = available_seats[0]  # Book the first available seat
        booked_seats[seat_number] = passenger_name  # Store the booking
        
        # Calculate the ticket price
        ticket_price = 100  # Price per seat
        total_cost = ticket_price  # Total cost for one ticket
        
        print(f"Ticket booked successfully! Seat number: {seat_number}")
    except ValueError:
        print("Invalid input. Please enter a numeric value for the flight number.")

if __name__ == "__main__":
    book_ticket()