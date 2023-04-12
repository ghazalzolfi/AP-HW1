from plane import Plane
class flight:
    def __init__(self, number, airplane_type, departure_time, arrival_time, status, passengers: list):
        self.number = number
        self.airplane_type = airplane_type
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.status = status
        self.passengers = passengers

    def add_passengers(self, passenger):
        self.passengers.append(passenger)
        print(f"{passenger} was added to passengers!")

    def remove_passengers(self, passenger):
        self.passengers.remove(passenger)
        print(f"{passenger} was remove from passengers!")

    def get_available_seats(self):
        pass

    def get_flight_duration(self):
        self.flight_duration = self.arrival_time - self.departure_time
        return  self.flight_duration
