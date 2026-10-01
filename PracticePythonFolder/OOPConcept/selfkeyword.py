#self keyword is used to represent the instance of the class.
#By using the "self" keyword we can access the attributes and methods of the class in python.

class Car:
    wheels=4
    def start_car(self):
        print("Car is starting")
        print(f"Car has {self.wheels} wheels")

    def example_method(self):
        print(self.wheels)

car1=Car()
print(car1.wheels)
car1.start_car()

car1.example_method()
