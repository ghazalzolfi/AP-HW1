from car import Car
from customer import Customer


class Rental:
    def __init__(self, pickup_date, return_date, total_fee, late_fee, car: Car, customer: Customer):
        self.pickup_date = pickup_date
        self.return_date = return_date
        self.total_fee = total_fee
        self.late_fee = late_fee
        # aggregation
        self.car = car
        self.customer = customer

    # aggregation  and composition (using customer and car class attributes)
    def extend_rental(self, new_return_date):
        self.return_date = new_return_date
        print(f"The rental for {self.car.model}extended for {self.customer.name} : {self.customer.customer_ID}!")

    def cancel_rental(self):
        print(f"Your rental canceled for {self.customer.name} : {self.customer.customer_ID}!")

    def calculate_late_fee(self, new_return_date):
        self.total_fee += (new_return_date - self.return_date)*self.late_fee
        return self.total_fee
