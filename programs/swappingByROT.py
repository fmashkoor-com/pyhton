#Swapping of two variables

	#Different ways
	#Using a temp variable
	#Using a formula
	#Using XOR operator
	#Using ROT_TWO (rotation-two) function

a = input("Enter 1st number: ")
b = input("Enter 2nd number: ")
print("-----------------------------")
a,b = b,a 
print("The value of 1st number is = " + str(a))
print("The value of 2nd number is = " + str(b))
