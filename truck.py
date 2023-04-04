from vehicle import Vehicle
class Truck(Vehicle):
    def __init__(self, license_plate, fuel_capacity, current_load, transmission_type):
        super().__init__(
            model, year, color, price, weight
        )
        self.license_plate = license_plate
        self.fuel_capacity = fuel_capacity
        self.current_load  = current_load
        self.transmission_type = transmission_type

    def load(self, weight):
        pass
    def unload(self, weight):
        pass
    def check_fuel(self):
        pass
    def check_load(self):
        pass