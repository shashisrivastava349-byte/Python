#static methods are methods that belong to the class rather than an instance of the class.
# They can be called on the class itself, rather than on an instance of the class.
# Static methods are defined using the @staticmethod decorator.

#instance methods are methods that belong to an instance of the class.

class Cars:
    # class variable
    wheels = 4

    def __init__(self, brand, model, price, milage):
        self.brand = brand  # instance variable
        self.model = model  # instance variable
        self.price = price  # instance variable
        self.milage = milage  # instance variable

    def get_car_info(self):
        print(self.brand, self.model, self.price, self.milage)  # accessing class variable

    @staticmethod
    def demo_car():
        print("demo car method called")

    @staticmethod
    def get_wheels():
        print(f"A car has {Cars.wheels} wheels.")  # accessing class variable
        Cars.demo_car()  # calling static method from another static method


toyotacar = Cars("Toyota", "Camry", 30000, 25)
toyotacar.get_car_info()  # calling instance method
Cars.get_wheels()  # calling static method






