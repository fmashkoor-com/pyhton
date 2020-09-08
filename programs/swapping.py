#Swapping of two variables

	#Different ways
	#Using a temp variable
	#Using a formula
	#Using XOR operator
	#Using ROT_TWO (rotation-two) function

a = 5
b = 6
print("The value of a is = " + str(a))
print("The value of b is = " + str(b))
print("-----------------------------")
print("Using temp variable")
print("-----------------------------")
c = a
a = b
b = c
print("The value of a is = " + str(a))
print("The value of b is = " + str(b))

a = 5
b = 6
print("-----------------------------")
print("Using formula")
#The drawback is that it take some extra bit
print("-----------------------------")
a = a + b  # a = 11 -> 0b1011 -> 4 bits
b = a - b  # b = 5 -> 0b101 -> 3 bits
a = a - b  # a = 6 -> 0b110 -> 3 bits
print("The value of a is = " + str(a))
print("The value of b is = " + str(b))

a = 5
b = 6
print("-----------------------------")
print("Using XOR")
print("-----------------------------")
a = a ^ b  # a = 3 -> 0b11 -> 2 bits
b = a ^ b  # b = 5 -> 0b101 -> 3 bits
a = a ^ b  # a = 6 -> 0b110 -> 3 bits
print("The value of a is = " + str(a))
print("The value of b is = " + str(b))

a = 5
b = 6
print("-----------------------------")
print("Using ROT_TWO funtion")
#https://stackoverflow.com/questions/21047524/how-does-swapping-of-members-in-tuples-a-b-b-a-work-internally
print("-----------------------------")
a,b = b,a 
print("The value of a is = " + str(a))
print("The value of b is = " + str(b))