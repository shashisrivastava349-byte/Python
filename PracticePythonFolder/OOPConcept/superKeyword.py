

# class A:
#     a=5
#     def sample(self):
#         print("Inside method A")
#
# class B(A):
#     a=10
#     def sample(self):
#         print("Inside method B")
#
#     def print_method(self):
#         print(super().a)
#         super().sample()
#
# obj=B()
# obj.print_method()


class A:
    def __init__(self):
        print("Inside __init__ method of class A")

class B(A):
    def __init__(self):
        super().__init__()
        print("Inside __init__ method of class B")

B()

