from vehicle import Vehicle
class Motorcycle(Vehicle):
    def __init__(self, transmission_type: str, mileage: int, is_running: bool, is_damaged: bool):
        super().__init__(
            model, year, color, price, weight , num_wheels
        )
        self.transmission_type = transmission_type
        self.mileage = mileage
        self.is_running = is_running
        self.is_damaged = is_damaged

    def set_mileage(self, mileage: int):
        self.mileage += mileage
        return self.mileage

    def set_is_running(self, is_running: bool):
        self.is_running = is_running
        print(f"is runing = {self.is_running}")

    def set_is_damaged(self, is_damaged: bool):
        self.is_damaged = is_damaged
        print(f"is damaged = {self.is_damaged}")

    def start(self):
        print("Turn on the ignition and press the starter button.")

    def stop(self):
        print("Press the kill switch to turn off the engine.")

    # overriding abstract method
    def get_num_wheels(self):
        print("I have two wheels!")


