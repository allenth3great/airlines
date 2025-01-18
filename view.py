from flight_data import flights

def view_flight_details(flight_number):
    flight = flights.get(flight_number)
    if flight:
        print("Flight Details:")
        print(f"- Destination: {flight['Destination']}")
        
        # Initialize booked seats if not already done
        if "Booked Seats" not in flight:
            flight["Booked Seats"] = {}
        
        booked_seats = flight["Booked Seats"]
        available_seats = flight["Seat Capacity"] - len(booked_seats)

        print(f"- Available Seats: {available_seats}")
        print("- Passengers:")
        
        if booked_seats:
            for seat, passenger in booked_seats.items():
                print(f"  {seat}. {passenger} (Seat: {seat})")
        else:
            print("  No passengers booked.")
    else:
        print("Flight not found.")

if __name__ == "__main__":
    try:
        flight_number = int(input("Enter flight number: "))
        view_flight_details(flight_number)
    except ValueError:
        print("Invalid input. Please enter a numeric value for the flight number.")