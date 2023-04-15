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

    def __find_passenger(self, passenger_name):
        founded_passenger = None
        for passenger in self.list_passengers:
            if passenger._name == passenger_name:
                founded_passenger = passenger
        return founded_passenger

    def remove_passengers(self, passenger_name):
        founded_passenger = self.__find_passenger(passenger_name)
        if founded_passenger:
            self.list_passengers.remove(passenger_name)
        print(f"{passenger_name} was remove from passengers!")

    # aggregation (using attribute of plane class)
    def get_available_seats(self, plane: Plane):
        available_seats_num = plane._passenger_capacity - len(self.list_passengers)
        print(f"There are {available_seats_num} empty seats!")

    def get_flight_duration(self):
        flight_duration = self.arrival_time - self.departure_time
        return flight_duration
