from vehicle import Vehicle
from wing import Wing
class Plane(Vehicle):
    def __int__(self,passenger_capacity: int, is_flying: bool, current_location: str, aircraft_company: float, wing, model, year, price, weight, num_wheels):
        super().__init__(model, year, price, weight, num_wheels)
        self.passenger_capacity = passenger_capacity
        self.is_flying = is_flying
        self.current_location = current_location
        self.aircraft_company = aircraft_company
        self.wing = Wing()

    def take_off(self):
        print("The airplane is taking off!")

    def land(self):
        print("The airplane is landing!")

    def fly_to(self,destination: str):
        print(f"The plane is flying to {destination}")

    def calculate_wing_loading(self):
        return self.weight / self.wing.calculate_surface_area()

    def get_current_location(self):
        return self.current_location

    # overriding abstract method
    def get_num_wheels(self):
        print("I have three wheels!")

