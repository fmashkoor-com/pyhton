#Operators in Python.

#Types of Operators
#Arithmetic Opertors
#Assignment Operators
#Relational Operators
#Logical Operators
#Unary Operators

x = 2.0
y = 3.0

print("------------------------------------------")
print("Arithmetic Operators")
print("----------------------")
print("Addition of two numbers = " + str(x + y))
print("Subtraction of two numbers = " + str(x - y))
print("Multiplication of two numbers = " + str(x * y))
print("Division of two numbers = " + str(x / y))

print("------------------------------------------")
print("Assignment Operators")
print("----------------------")
x += 2
print("Increment by 2 = " + str(x)) #x=x+2
y *= 2
print("Multiple by 3 = " + str(y)) #y=y*2
a,b = 5,6
print(a, b)

print("------------------------------------------")
print("Unary Operators")
print("----------------------")
n = 7
print("The value of n is = " + str(n))
print("The value of -n is = " + str(-n))
n = -n
print("n is equal to -n now the value of n is = " + str(n))

print("------------------------------------------")
print("Relational Operators")
print("----------------------")
print("The value of a is less than b = " + str(a<b))
#Compare
print("Are the values of a and b are equal = " + str(a == b)) 
#Less than or equal
print("Are the value of a is less than pr equal to b = " + str(a<=b))
#Not Equal
print("The values of a and b are not equal = " + str(a!=b))

print("------------------------------------------")
print("Logical Operators")
print("----------------------")
a=5
b=4
print("The value of 'a' should be less than 6 and 'b' is less than 5 = " + str(a<8 and b<5))
print("The value of 'a' should be less than 6 and 'b' is less than 5 = " + str(a<8 and b<2))
print("The value of 'a' should be less than 6 or 'b' is less than 5 = " + str(a<8 or b<1))
print("The value of 'a' should be less than 6 or 'b' is less than 5 = " + str(a>8 or b<1))
z = True
print("The value of z is = " + str(z))
print("After applying Not operator the value of z is = " + str(not z))