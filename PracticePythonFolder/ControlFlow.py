#Control flow exercises

#selection/Decision
#if statement
#if statement with else
#if statement with elif

#repetition/loops
#for loop
#while loop

#Transfer of control / jump statements
#break statement
#continue statement
#pass statement
#return statement
#try and except statement



#1. Write a program that asks the user to enter a number and prints whether the number is positive, negative, or zero.
number = float(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")