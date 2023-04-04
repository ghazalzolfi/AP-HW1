class Rental:
    def __init__(self, pickup_date, return_date, total_fee, late_fee):
        self.pickup_date = pickup_date
        self.return_date = return_date
        self.total_fee = total_fee
        self.late_fee = late_fee

    def extend_rental(self, return_date):
        pass
    def cancel_rental(self):
        pass
    def calculate_late_fee(self):
        pass
