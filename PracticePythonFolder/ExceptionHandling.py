

print("Start of the program")

print("Enter any number:")
num = int(input())

try:
    a=10/num

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

else:
    print("In the else block of the program")

finally:
    print("In the finally block of the program")

print("End of the program")