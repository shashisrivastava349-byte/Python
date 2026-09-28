#operators are used to perform operations on variables and values.
# In Python, there are several types of operators, including:

# 1. Arithmetic operators are used to perform mathematical operations such as
# addition, subtraction, multiplication, and division.

# 2. Comparison operators are used to compare two values and return a Boolean value (True or False) based on the comparison.

# 3. Logical operators are used to combine multiple Boolean expressions and
# return a Boolean value based on the result of the combination.

# 4. Assignment operators are used to assign values to variables.

# 1. Arithmetic operators
a=50
b=10
print(a+b)
print(a-b)
print(a*b)
print(a/b) #true division gives the quotient as a floating-point number
print(a//b) #floor division gives the quotient without the remainder
print(a%b) #modulus give the remainder

# 2. Comparison operators
print(a > b)  # greater than
print(a < b)  # less than
print(a == b) # equal to
print(a != b) # not equal to
print(a >= b) # greater than or equal to
print(a <= b) # less than or equal to

# 3. Logical operators
print(a and b) # logical AND
print(a or b)  # logical OR
print(not a)   # logical NOT

# 4. Assignment operators
c = 5
print(c)
c = c + 5 # equivalent to c += 5
print(c)
c = c - 5 # equivalent to c -= 5
print(c)
c = c * 5 # equivalent to c *= 5
print(c)
c = c / 5  # equivalent to c /= 5
print(c)

#operator precedence determines the order in which operations are performed in an expression.
# In Python, the order of precedence is as follows:
# 1. Parentheses
# 2. Exponentiation
# 3. Multiplication, Division, Floor Division, Modulus
# 4. Addition, Subtraction

print(5*2+3/5) # multiplication and division are performed before addition
print((5*2)+(3/5)-1) # parentheses override the default precedence
print(2*2**4) # exponentiation is performed before multiplication
print(8*3/2%7//3) # multiplication, division, modulus, and floor division are performed from left to right

