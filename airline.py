from flight import Flight
from plane import Plane


class Airline:
    def __init__(self, name, country, code, flights: list, employees: list, planes: list):
        self.name = name
        self.country = country
        self.code = code
        self.flights = flights
        self.employees = employees
        self.planes = planes

    # aggregation
    # composition
    def add_flight(self, flight: Flight, plane: Plane):
        self.flights.append(flight)
        self.planes.append(plane)
        print(f"{flight} : {plane} is added to {self} airline!")

    def __find_flight(self, flight_number):
        founded_flight = None
        for flight in self.flights:
            if flight.number == flight_number:
                founded_flight = flight
        return founded_flight

    def remove_flight(self, flight_number):
        founded_flight = self.__find_flight(flight_number)
        if founded_flight:
            self.flights.remove(flight_number)
        return founded_flight

    def get_flights(self):
        return self.flights
