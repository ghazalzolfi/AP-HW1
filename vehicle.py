from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, model, year, color, price, weight):
        self.model = model
        self.year = year
        self.color = color
        self.price = price
        self.weight = weight
        self.speed = 0
        self.fuel = 0

    def accelerate(self, final_speed : float):
        self.speed = final_speed
        print(f"accelerating! Your speed is {self.speed}")

    def brake(self, final_speed: float):
        self.speed = final_speed
        print(f"braking! Your speed is {self.speed}")

    def turn(self, direction: str):
        pass

    def honk_horn(self):
        print("Honking!")

    def refuel(self, amount: float):
        self.fuel += amount
        print(f"refueling!")