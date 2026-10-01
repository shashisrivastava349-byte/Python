#Polymorphism in python
#Overriding

class A:
    a=5

    def samples(self):
        print("Parent method")

class B(A):
    a=10

    def samples(self):
        print("Child method")

obj=B()
print(obj.a)
obj.samples()


