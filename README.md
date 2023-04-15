Ghazal Zolfi Moselo

Advanced Programming HW1


موضوع انتخابی من برای این تمرین، وسایل نقلیه است.
با تعریف کلاس وسایل نقلیه که یک "کلاس انتزاعی" است، شروع کردم. در کلاس وسایل نقلیه با به‌کار گیری مفهوم "پلی‌مورفیسم" دو متود استارت و استاپ را در کلاس مادر تعریف کردم. کلاس‌های فرزند موتور، ماشین، هواپیما، وانت و کشتی از کلاس مادر وسایل نقلیه "ارث‌بری" می‌کنند. هم‌چنین برای فرا خوانی متودهای استارت و استاپ آن‌ها را در کلاس‌های فرزند "بازخوانی" کرده و برای هرکدام از آنها این متود خروجی متفاوتی دارد.

vehicle class:
#polymorphism (defining methods in parent class)

    def start(self):
        pass

    def stop(self):
        pass
car class:
#polymorphism (defining methods in child class)

    def start(self):
        print("Insert key, turn ignition, and press gas pedal to start.")

    def stop(self):
        print("Put car in park, turn off ignition, and remove key.")

motorcycle class:
#polymorphism (defining methods in child class)

    def start(self):
        print("Turn on the ignition and press the starter button.")

    def stop(self):
        print("Press the kill switch to turn off the engine.")

با تعریف کلاس موتور و استفاده از آن در کلاس‌های موتور و ماشین از مفهوم "کامپوزیشن" استفاده کردم. این رابطه برای موتور ماشین و خود کلاس ماشین به این صورت است که با تعریف کلاس ماشین، موتور آن را هم به عنوان ورودی دریافت می‌کنیم. و دو متود استارت موتور در کلاس ماشین زمانی که ماشین استارت می‌خورد، متود استارت موتور ماشین نیز فراخوانی می‌شود. 

car class:
#composition (using method of engine class)

    def start_engine(self):
        self.engine.start()
        print(f"Your {self} is ready to go!")
با تعریف کلاس اونر و تعریف دو لیست یکی برای ماشین‌های آن فرد و یکی برای موتورهای او، از متودی برای اضافه و کم کردن شی موتور و شی ماشین به لیست‌های مورد نظر استفاده می‌کنیم. در اینحا از مفهوم "اگریگیشن" استفاده کرده‌ایم. در اینجا برای حذف کردن یک شی ماشین و یا شی موتور، یک "متود پرایوت" برای پیدا کردن ماشین موردنظر، تعریف می‌کنیم که فقط در همین کلاس کاربرد دارد. و با فراخوانی این تابع می‌توانیم شی ماشین مورد نظر را پیدا کرده و از لیست حذف کنیم.

owner class:

    def add_car(self, car: Car):
        self.cars.append(car)
        return self.cars

    def __find_car(self, car_model):
        founded_car = None
        for car in self.cars:
            if car.model == car_model:
                founded_car = car
        return founded_car

    def remove_car(self, car_model):
        founded_car = self.__find_car(car_model)
        if founded_car:
            self.cars.remove(founded_car)
        return founded_car

در کلاس رنتال برای اجاره دادن ماشین‌ها می دانیم که هرقرار دادی برای اجاره یک مشتری و یک ماشین برای اجاره دادن را شامل می‌شود.

rental class:
#aggregation  and composition (using customer and car class attributes)

    def extend_rental(self, new_return_date):
        self.return_date = new_return_date
        print(f"The rental for {self.car.model}extended for {self.customer.name} : {self.customer.customer_ID}!")

    def cancel_rental(self):
        print(f"Your rental canceled for {self.customer.name} : {self.customer.customer_ID}!")

در کلاس هواپیما با استفاده از مفهوم "اگریگیشن" از کلاس بال استفاده کردیم. و برای محاسبه‌ی لود بال هواپیما از متود محاسبه‌ی مساحت بهره بردیم.

plane class:
#aggregation (using a method of wing class)

    def calculate_wing_loading(self):
        return self.weight / self.wing.calculate_surface_area()

در کلاس ایرلاین برای متود اضافه و حذف کردن پرواز، در کلاس شرکت هواپیمایی برای اضافه یا حذف کردن هواپیما و در کلاس فلایت برای اضافه و یا حذف کردن مسافر به حالتی مشابه هم عمل می‌کنیم. برای مثال، به این صورت:

flight class:
#aggregation (using method of passenger class)

    def add_passengers(self, passenger: Passenger):
        self.list_passengers.append(passenger)
        passenger.send_email()
        print(f"{passenger} was added to passengers!")

    def __find_passenger(self, passenger_name):
        founded_passenger = None
        for passenger in self.list_passengers:
            if passenger._name == passenger_name:
                founded_passenger = passenger
        return founded_passenger

    def remove_passengers(self, passenger_name):
        founded_passenger = self.__find_passenger(passenger_name)
        if founded_passenger:
            self.list_passengers.remove(passenger_name)
        print(f"{passenger_name} was remove from passengers!")

