from vehicle import Vehicle

class Plane(vehicle):
    def __int__(self,passenger_capacity: int, is_flying: bool, current_location: str, aircraft_company: float, wing):
        super().__init__(
            model, year, color, price, weight
        )
        self.passenger_capacity = passenger_capacity
        self.is_flying = is_flying
        self.current_location = current_location
        self.aircraft_company = aircraft_company
        self.wing = wing

    def take_off(self):
        pass

    def land(self):
        pass

    def fly_to(self,destination: str):
        pass

    def get_current_location(self):
        pass

