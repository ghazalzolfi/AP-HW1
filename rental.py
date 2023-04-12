class Rental:
    def __init__(self, pickup_date, return_date, total_fee, late_fee):
        self.pickup_date = pickup_date
        self.return_date = return_date
        self.total_fee = total_fee
        self.late_fee = late_fee

    def extend_rental(self, new_return_date):
        self.return_date = new_return_date
        print("Your rental extended!")
    def cancel_rental(self):
        print("Your rental canceled!")
    def calculate_late_fee(self, new_return_date):
        self.total_fee += (new_return_date-self.return_date)*self.late_fee
        return self.total_fee
