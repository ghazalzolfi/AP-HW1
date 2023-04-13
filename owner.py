from car import Car
from motorcycle import Motorcycle
class Owner:
    def __init__(self, name, address, phone_number, email, **kwargs):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        # the constructor accepts any additional keyword arguments.
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.cars = []
        self.motorcycles = []
        # aggregation
        self.car = Car()
        self.motorcycle = Motorcycle()

    def add_car(self, car: Car):
        self.cars.append(car)
        return self.cars
    def remove_car(self, car: Car):
        self.cars.remove(car)
        return self.cars

    def add_motorcycle(self, motorcycle: Motorcycle):
        self.motorcycles.append(motorcycle)
        return self.motorcycles
    def remove_motorcycle(self, motorcycle: Motorcycle):
        self.motorcycles.remove(motorcycle)
        return self.motorcycles