#InBuild Function in Python
#To use the inbuilt funciton we need to import the lib.

import math

#SquareRoot 
x = math.sqrt(25)
print("Square root of 25 = " + str(x))
y = math.sqrt(15)
print("Square root of 15 = " + str(y))

#Floor
print("---------------")
print("floor")
print(math.floor(2.5))
print(math.floor(3.9))

#Ceil
print("---------------")
print("ceil")
print(math.ceil(2.5))
print(math.ceil(3.9))

#Power
print("---------------")
print("Power of number")
print(3**2)
print(math.pow(3,2))

#Pi
print("---------------")
print("value of Pi = " + str(math.pi))

#Using alias instead of math 
import math as m
print("---------------")
print("SquareRoot of 36 = " + str(m.sqrt(36)))

#If we only want to import specific function of math like power or sqrt
from math import sqrt, pow
print("---------------")
print(pow(2,3))