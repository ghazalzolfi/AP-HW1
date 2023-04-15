from plane import Plane
from passenger import Passenger


class Flight:
    def __init__(self, number, airplane_type, departure_time, arrival_time, status, list_passengers: list):
        self.number = number
        self.airplane_type = airplane_type
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.status = status
        self.list_passengers = list_passengers

    # aggregation (using method of passenger class)
    def add_passengers(self, passenger: Passenger):
        self.list_passengers.append(passenger)
        passenger.send_email()
        print(f"{passenger} was added to passengers!")

    def remove_passengers(self, passenger: Passenger):
        self.list_passengers.remove(passenger)
        passenger.send_email()
        print(f"{passenger} was remove from passengers!")

    # aggregation (using attribute of plane class)
    def get_available_seats(self, plane: Plane):
        available_seats_num = plane._passenger_capacity - len(self.list_passengers)
        print(f"There are {available_seats_num} empty seats!")

    def get_flight_duration(self):
        flight_duration = self.arrival_time - self.departure_time
        return flight_duration
