
class Car:

    def initialization_method(self, brand, model, price,milage):
        self.brand = brand
        self.model = model
        self.price = price
        self.milage = milage

    def start_car(self):
        print(self.brand + " car having model as" + self.model+ "has started")

    def stop_car(self):
        print(self.brand + " car having model as" + self.model+ "has stopped")

    def print_method(self):
        print("Brand of the car: " + self.brand)
        print("Model of the car: " + self.model)
        print("Price of the car: " + str(self.price))
        print("Milage of the car: " + str(self.milage))
        print("----------------------------------------------------")

toyota=Car()
toyota.initialization_method("Toyota", "Camry", 25000, 30)
toyota.start_car()
toyota.stop_car()
toyota.print_method()

hundai=Car()
hundai.initialization_method("Hyundai", "Elantra", 20000, 35)
hundai.start_car()
hundai.stop_car()
hundai.print_method()

suzuki=Car()
suzuki.initialization_method("Suzuki", "Swift", 15000, 40)
suzuki.start_car()
suzuki.stop_car()
suzuki.print_method()
