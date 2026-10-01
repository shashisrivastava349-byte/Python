#Method parameters are the variables that are passed to a method when it is called.
#They allow you to pass data into a method so that it can perform operations on that data.
#In Python, you can define methods with parameters by including them in the method definition.

class Car:
    wheels = 4

    def start_car(self):
        print("Car started")

    def sample(self, brand, model, price, year):
        self.brand = brand #creating instance variables to store the values of the parameters
        self.model = model #class level variables
        self.price = price
        self.year = year
        print(brand, model,price,year)

    def sample2(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Price: ${self.price}, Year: {self.year}")
        print(self.wheels)

    def sample3(self):
        print(self.wheels)
        self.start_car()

car1=Car()
car1.sample("Toyota", "Camry", 25000, 2020)
car1.sample2()
car1.sample3()
