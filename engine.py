class Engine:
    def __init__(self, cylinders, horsepower, fuel_type, displacement):
        self.cylinders = cylinders
        self.horsepower = horsepower
        self.fuel_type = fuel_type
        self.displacement = displacement

    def get_cylinders(self):
        return self.cylinders
    def set_cylinders(self, cylinders):
        self.cylinders = cylinders
    def start(self):
        print("Starting the engine.")
    def stop(self):
        print("Stopping the engine.")
