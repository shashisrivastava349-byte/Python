#Inheritance is a way to form new classes using classes that have already been defined.
# The newly formed classes are called derived classes, the classes that we derive from are called base classes.

class A:

    a=10
    def feature1(self):
        print("Feature 1 is working")

    def feature2(self):
        print("Feature 2 is working")

class B(A):  # Class B is derived from class A

    b=20
    def feature3(self):
        print("Feature 3 is working")

    def feature4(self):
        print("Feature 4 is working")

child=B()  # Creating an object of class B
child.feature1()  # Calling feature1 from class A
child.feature2()  # Calling feature2 from class A
child.feature3()  # Calling feature3 from class B
child.feature4()  # Calling feature4 from class B

print(child.a)
print(child.b)