from vehicle import Vehicle
class Plane(vehicle):
    def __int__(self,passenger_capacity: int, is_flying: bool, current_location: str, aircraft_company: float, wing):
        super().__init__(
            model, year, color, price, weight, num_wheels
        )
        self.passenger_capacity = passenger_capacity
        self.is_flying = is_flying
        self.current_location = current_location
        self.aircraft_company = aircraft_company
        self.wing = wing

    def take_off(self):
        print("The airplane is taking off!")

    def land(self):
        print("The airplane is landing!")

    def fly_to(self,destination: str):
        print(f"The plane is flying to {destination}")

    def get_current_location(self):
        return self.current_location

    # overriding abstract method
    def get_num_wheels(self):
        print("I have three wheels!")

