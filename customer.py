class Customer:
    def __init__(self, customer_ID, name, address, phone_number, license_num):
        self._customer_ID = customer_ID
        self._name = name
        self.__address = address
        self.__phone_number = phone_number
        self._license_num = license_num

    def make_reservation(self):
        print("Reservation made!")
    def cancel_reservation(self):
        print("Reservation cancled!")

    def view_transactions(self):
        pass