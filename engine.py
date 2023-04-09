class Engine:
    def __init__(self, cylinders, horsepower, fuel_type, displacement):
        self.cylinders = cylinders
        self.horsepower = horsepower
        self.fuel_type = fuel_type
        self.displacement = displacement

    def get_cylinders(self):
        pass
    def set_cylinders(self):
        pass
    def start(self):
        print("Starting the engine.")
    def stop(self):
        print("Stopping the engine.")
