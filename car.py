from vehicle import Vehicle
class Car(Vehicle):
    def __init__(self,num_of_doors: int, num_of_wheels: int, max_speed: int, current_gear: int, engine):
        super().__init__(
            model, year, color, price, weight, num_wheels
        )
        self.num_of_doors = num_of_doors
        self.num_of_wheels = num_of_wheels
        self.max_speed = max_speed
        self.current_gear = current_gear
        self.engine = engine


    def start_engine(self):
        print(f"Your {self} is ready to go!")

    def lock_doors(self):
        print(f"{self}'s doors are locked!")

    def unlock_doors(self):
        print(f"{self}'s doors are unlocked!")

    def change_gears(self, final_gear: int):
        self.current_gear = final_gear
        print(f"Your current gear is {self.current_gear}")

    # overriding abstract method
    def get_num_wheels(self):
        print("I have four wheels!")






