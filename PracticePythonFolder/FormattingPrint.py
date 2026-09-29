#Formatting Print
#Write a program that prints the following string in a specific format (see the output).
print("Twinkle, twinkle, little star,")
print("\tHow I wonder what you are!")
print("\t\tUp above the world so high,")
print("\t\tLike a diamond in the sky.")

name="Shashi"
age=20
location="Bangalore"
# print("my name is "+name+" and my age is "+str(age)+" and I live in "+location)
# print("my name is "+name+" and my age is ",age," and I live in "+location)
print(f"my name is {name} and my age is {age} and I live in {location}")
print("My name is {} and my age is {} and I live in {}".format(name,age,location))
print("My name is %s and my age is %d and I live in %s" % (name, age, location))
