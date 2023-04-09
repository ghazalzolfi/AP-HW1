from vehicle import Vehicle
class Motorcycle(vehicle):
    def __init__(self, transmission_type: str, mileage: int, is_running: bool, is_damaged: bool):
        super().__init__(
            model, year, color, price, weight , num_wheels
        )
        self.transmission_type = transmission_type
        self.mileage = mileage
        self.is_running = is_running
        self.is_damaged = is_damaged

    def get_mileage(self):
        pass

    def set_mileage(self, mileage: int):
        pass

    def set_is_running(self, is_running: bool):
        pass

    def set_is_damaged(self, is_damaged: bool):
        pass

    # overriding abstract method
    def get_num_wheels(self):
        print("I have two wheels!")


