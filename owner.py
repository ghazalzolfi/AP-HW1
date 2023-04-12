class Owner:
    def __init__(self, name, address, phone_number, email):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.cars = []
        self.motorcycles = []

    def add_car(self, car: str):
        self.cars.append(car)
        return self.cars
    def remove_car(self, car: str):
        self.cars.remove(car)
        return self.cars

    def add_motorcycle(self, motorcycle: str):
        self.motorcycles.append(motorcycle)
        return self.motorcycles
    def remove_motorcycle(self, motorcycle: str):
        self.motorcycles.remove(motorcycle)
        return self.motorcycles