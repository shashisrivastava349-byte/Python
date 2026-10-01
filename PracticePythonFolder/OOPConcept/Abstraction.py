from abc import ABC, abstractmethod


#Abstract class
class A(ABC):

    def __init__(self, a):
        self.a=a

    # Abstract method
    @abstractmethod
    def method(self):
        pass

    @abstractmethod
    def method2(self):
        pass

    def method3(self):
        print("Inside method 3.")

class B(A):
    def method(self):
        print("Inside method 1.",self.a)

    def method2(self):
        print("Inside method 2.")

obj=B(5)
obj.method()
obj.method2()
obj.method3() ## Accsesing the method of abstract class using child class object.
