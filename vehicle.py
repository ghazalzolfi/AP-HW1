from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, model: str, year: int, color: str, price: float, weight: float, num_wheels: int, **kwargs):
        self.model = model
        self.year = year
        self.color = color
        self.price = price
        self.weight = weight
        self.num_wheels = num_wheels
        self.speed = 0
        self.fuel = 0
#       the constructor accepts any additional keyword arguments.
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return f"{self.model} {self.year} {self.color}"

    def accelerate(self, final_speed: float):
        self.speed = final_speed
        print(f"accelerating! Your speed is {self.speed}")

    def brake(self, final_speed: float):
        self.speed = final_speed
        print(f"braking! Your speed is {self.speed}")

    @staticmethod
    def honk_horn():
        print("Honking!")

    def refuel(self, amount: float):
        self.fuel += amount
        print(f"refueling!")

#   polymorphism (defining methods in parent class)
    def start(self):
        print("Rٍٍeady to go!")

    def stop(self):
        print("Stopping!")

#   defining abstract method in parent class
    @abstractmethod
    def get_num_wheels(self):
        pass
