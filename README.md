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


با تعریف کلاس اونر و تعریف دو لیست یکی برای ماشین‌های آن فرد و یکی برای موتورهای او
