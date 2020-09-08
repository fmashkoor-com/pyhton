#Swapping of two variables

	#Different ways
	#Using a temp variable
	#Using a formula
	#Using XOR operator
	#Using ROT_TWO (rotation-two) function

a = input("Enter 1st number: ")
b = input("Enter 2nd number: ")
#The drawback is that it take some extra bit
print("-----------------------------")
# Consider a=5, b=6
a = a + b  # a = 11 -> 0b1011 -> 4 bits
b = a - b  # b = 5 -> 0b101 -> 3 bits
a = a - b  # a = 6 -> 0b110 -> 3 bits
print("The value of 1st number is = " + str(a))
print("The value of 2nd number is = " + str(b))
