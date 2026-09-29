#Local and Global Variables
x = 10  # Global variable

def print_values():
    y = 20  # Local variable
    print(x)  # Accessing global variable
    print(y)  # Accessing local variable

print_values()
print(x)  # Accessing global variable
print(y)  # This will cause an error because y is a local variable
