from plane import Plane
class flight:
    def __init__(self, number, airplane_type, departure_time, arrival_time, status, passengers):
        self.number = number
        self.airplane_type = airplane_type
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.status = status
        self.passengers = passengers

    def add_passengers(self, passenger):
        pass

    def remove_passengers(self, passenger):
        pass

    def get_available_seats(self):
        pass

    def get_flight_duration(self):
        pass

    def get_flight_distance(self):
        pass
