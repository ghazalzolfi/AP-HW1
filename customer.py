class Customer:
    def __init__(self, customer_ID, name, address, phone_number, license_num, **kwargs):
        # define protected and private attributes
        self.customer_ID = customer_ID
        self.name = name
        self.__address = address
        self.__phone_number = phone_number
        self._license_num = license_num
        # the constructor accepts any additional keyword arguments.
        for key, value in kwargs.items():
            setattr(self, key, value)

    @staticmethod
    def make_reservation():
        print("Reservation made!")

    @staticmethod
    def cancel_reservation():
        print("Reservation cancled!")

    def view_transactions(self):
        print("Here is your transactions!")
