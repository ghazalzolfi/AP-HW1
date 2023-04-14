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

    def add_car(self, car: Car):
        self.cars.append(car)
        return self.cars

    def __find_car(self, car_model):
        founded_car = None
        for car in self.cars:
            if car.model == car_model:
                founded_car = car
        return founded_car

    def remove_car(self, car_model):
        founded_car = self.__find_car(car_model)
        if founded_car:
            self.cars.remove(founded_car)
        return founded_car

    def add_motorcycle(self, motorcycle: Motorcycle):
        self.motorcycles.append(motorcycle)
        return self.motorcycles

    def __find_motorcycle(self, motorcycle_model):
        founded_motorcycle = None
        for motorcycle in self.motorcycles:
            if motorcycle.model == motorcycle_model:
                founded_motorcycle = motorcycle
        return founded_motorcycle

    def remove_motorcycle(self, motorcycle_model):
        founded_motorcycle = self.__find_motorcycle(motorcycle_model)
        if founded_motorcycle:
            self.motorcycles.remove(founded_motorcycle)
        return founded_motorcycle
