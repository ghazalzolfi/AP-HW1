class Vehicle:
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
        print(f"")

    def turn(self, direction: string):
        pass

    def honk_horn(self):
        pass

    def refuel(self, amount: float):
        fuel += amount
        print(f"")