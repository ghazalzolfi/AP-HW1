from vehicle import Vehicle
class Ship(Vehicle):
    def __init__(self, captain, fuel_efficiency, is_moving, safety_rating, model, year, price, weight, num_wheels):
        super().__init__(model, year, price, weight, num_wheels)
        self.captain = captain
        self.fuel_efficiency = fuel_efficiency
        self.is_moving = is_moving
        self.safety_rating = safety_rating

    def get_safty_rating(self):
        return self.safety_rating
    def set_safty_rating(self, safety_rating):
        self.safety_rating = safety_rating
        return self.safety_rating
    def set_is_moving(self, is_moving):
        self.is_moving = is_moving
        return self.is_moving

    # overriding abstract method
    def get_num_wheels(self):
        print("I have no wheels!")
