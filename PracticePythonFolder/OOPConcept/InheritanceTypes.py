#Types of Inheritance in Python
# Single Inheritance
# class A:
#     a=9
#
# class B(A):
#     b=10
#
# obj=B()
# print(obj.a)
# print(obj.b)


# Multiple Inheritance
# class A:
#     a=9
#
# class B:
#     b=10
#
# class C(A, B):
#     c=11
#
# obj=C()
# print(obj.a)
# print(obj.b)
# print(obj.c)


# Multilevel Inheritance
# class A:
#     a=9
#
# class B(A):
#     b=10
#
# class C(B):
#     c=11
#
# obj=C()
# print(obj.a)
# print(obj.b)
# print(obj.c)


# Hierarchical Inheritance
# class A:
#     a=9
# class B(A):
#     b=10
# class C(A):
#     c=11
#
# obj=B()
# print(obj.a)
# print(obj.b)
# obj1=C()
# print(obj1.a)
# print(obj1.c)


# Hybrid Inheritance
class A:
    a=9
class B(A):
    b=10
class C(A):
    c=20
class D(B, C):
    d=30
obj=D()
print(obj.a)
print(obj.b)
print(obj.c)
print(obj.d)