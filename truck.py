from vehicle import Vehicle
class Truck(Vehicle):
    def __init__(self, license_plate: str, fuel_capacity: float, current_load: float, transmission_type: str, model, year, color, price, weight, num_wheels):
        super().__init__(
            model, year, color, price, weight, num_wheels
        )
        self.license_plate = license_plate
        self.fuel_capacity = fuel_capacity
        self.current_load  = current_load
        self.transmission_type = transmission_type

    def load(self, weight: float):
        self.current_load += weight
        print(f"Loading! Your current load is {self.current_load}.")
    def unload(self, weight: float):
        self.current_load -= weight
        print(f"Unloading! Your current load is {self.current_load}!")
    def check_load(self):
        return self.current_load
    # overriding abstract method
    def get_num_wheels(self):
        print("I may have four to eighteen wheels!")
    