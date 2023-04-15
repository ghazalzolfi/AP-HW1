from vehicle import Vehicle


class Truck(Vehicle):
    def __init__(self, license_plate: str, fuel_capacity: float, current_load: float, transmission_type: str,
                 model, year, color, price, weight, num_wheels):
        super().__init__(model, year, color, price, weight, num_wheels)
        self.license_plate = license_plate
        self.fuel_capacity = fuel_capacity
        self.current_load = current_load
        self.transmission_type = transmission_type

#   using attributes of parent class
    def load(self, weight: float):
        self.current_load += weight
        total_weight = self.weight + self.current_load
        print(f"Loading! Your total weight is {total_weight}.")

    def unload(self, weight: float):
        self.current_load -= weight
        total_weight = self.weight + self.current_load
        print(f"Unloading! Your total weight is {total_weight}!")

    def check_load(self):
        return self.current_load

    # polymorphism (defining methods in child class)
    def start(self):
        print("Your truck is ready to go!")

    def stop(self):
        print("Your truck was stopped!")

    # overriding abstract method
    def get_num_wheels(self):
        print("I may have four to eighteen wheels!")
    