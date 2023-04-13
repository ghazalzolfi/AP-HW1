class Customer:
    def __init__(self, customer_ID, name, address, phone_number, license_num, **kwargs):
        # define protected and private attributes
        self._customer_ID = customer_ID
        self._name = name
        self.__address = address
        self.__phone_number = phone_number
        self._license_num = license_num
        # the constructor accepts any additional keyword arguments.
        for key, value in kwargs.items():
            setattr(self, key, value)

    def make_reservation(self):
        print("Reservation made!")
    def cancel_reservation(self):
        print("Reservation cancled!")

    def view_transactions(self):
        print("Here is your transactions!")