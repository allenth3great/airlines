from flight_data import flights

def generate_flight_report():
    try:
        flight_number = int(input("Enter flight number: "))
        
        # Check if the flight exists
        if flight_number not in flights:
            print("Flight not found.")
            return
        
        flight_info = flights[flight_number]
        destination = flight_info["Destination"]
        total_seats = flight_info["Seat Capacity"]
        
        # Initialize booked seats if not already done
        if "Booked Seats" not in flight_info:
            flight_info["Booked Seats"] = {}
        
        booked_seats = flight_info["Booked Seats"]
        booked_count = len(booked_seats)
        available_seats = total_seats - booked_count
        
        # Calculate revenue
        ticket_price = 100  # Price per seat
        revenue = booked_count * ticket_price
        
        # Display the report
        print("\nFlight Report:")
        print(f"- Destination: {destination}")
        print(f"- Total Seats: {total_seats}")
        print(f"- Booked Seats: {booked_count}")
        print(f"- Available Seats: {available_seats}")
        print(f"- Revenue: ${revenue:.2f}")
        
    except ValueError:
        print("Invalid input. Please enter a numeric value for the flight number.")

if __name__ == "__main__":
    generate_flight_report()