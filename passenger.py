class Passenger:
    def __init__(self, name, pass_num, birthdate, email):
        # define protected attributes
        self._name = name
        self._pass_num = pass_num
        self._birthdate = birthdate
        self._email = email
        self.checked_in = None

    def get_detail(self):
        print(f"passenger name : {self._name} and passenger passport number : {self._pass_num}")

    def send_email(self):
        print("Click to see your reservation status! ")

    def check_in(self):
        self.checked_in = True
        print(f"{self._name} was checked in!")
