from vehicle import Vehicle
from wing import Wing


class Plane(Vehicle):
    def __int__(self, passenger_capacity: int, is_flying: bool, current_location: str, aircraft_company: float,
                model, year, price, weight, num_wheels,
                length, width, thickness, material):
        super().__init__(model, year, price, weight, num_wheels)
        # define protected(passenger_capacity) and private(is_flying, current_location) attributes
        self._passenger_capacity = passenger_capacity
        self.__is_flying = is_flying
        self.__current_location = current_location
        self.aircraft_company = aircraft_company
        # aggregation
        self.wing = Wing(length, width, thickness, material)

    @staticmethod
    def take_off():
        print("The airplane is taking off!")

    @staticmethod
    def land():
        print("The airplane is landing!")

    @staticmethod
    def fly_to(destination: str):
        print(f"The plane is flying to {destination}")

    # aggregation (using a method of wing class)
    def calculate_wing_loading(self):
        return self.weight / self.wing.calculate_surface_area()

    def get_current_location(self):
        print(f"Plane's current location is {self.__current_location}")

    # overriding abstract method
    def get_num_wheels(self):
        print("I have three wheels!")
