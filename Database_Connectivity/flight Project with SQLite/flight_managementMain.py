import sqlite3
from flight import Flight

def retrieve_flight_by_id(flight_id, conn):
    cursor = conn.cursor()
    cursor.execute(
        "SELECT flightId, source, destination, noofseats, flightfare FROM flight WHERE flightId = ?",
        (flight_id,)
    )

    row = cursor.fetchone()

    if row:
        return Flight(row[0], row[1], row[2], row[3], row[4])
    else:
        return None


def main():
    conn = sqlite3.connect("flight.db")   # Database connection

    flight_id = int(input("Enter the flight id:"))

    flight = retrieve_flight_by_id(flight_id, conn)

    if flight:
        print("\nFlight details are:\n")
        print("Flight ID:", flight.get_flight_id())
        print("Source:", flight.get_source())
        print("Destination:", flight.get_destination())
        print("No of seats:", flight.get_no_of_seats())
        print("Flight Fare:", flight.get_flight_fare())
    else:
        print("Invalid Flight ID")

    conn.close()


if __name__ == "__main__":
    main()
