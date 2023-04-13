from plane import Plane
class flight:
    def __init__(self, number, airplane_type, departure_time, arrival_time, status, passengers: list, passenger_capacity):
        self.number = number
        self.airplane_type = airplane_type
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.status = status
        self.passengers = passengers
        self.plane = Plane(passenger_capacity)

    def add_passengers(self, passenger):
        self.passengers.append(passenger)
        print(f"{passenger} was added to passengers!")

    def remove_passengers(self, passenger):
        self.passengers.remove(passenger)
        print(f"{passenger} was remove from passengers!")

    def get_available_seats(self):
        available_seats_num = self.plane.passenger_capacity - len(self.passengers)
        print(f"There are {available_seats_num} empty seats!")

    def get_flight_duration(self):
        flight_duration = self.arrival_time - self.departure_time
        return  flight_duration
