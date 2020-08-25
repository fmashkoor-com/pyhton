#(Ctrl + B to run the script)

#DataTypes in Python
#None 
#Numeric
#Sequence
#Dictonary

# ----------------------------------------------------------------------------------------------- #
# 1) None is like null
# 2) Numeric 
		   #int
		   #float
		   #complex  realNum+imaginaryNum (6+4j) 
		   #bool
# a)Int		   
i = 5
print(type(i))   
# b)Float
f = 2.5
print(type(f))
# c)Complex
c = 6 + 9j
print(type(c))

#Convert float to int
a = 5.6
b = int(a)
print(type(b))
print(b)

#Convert int to float
print(float(b))

#Convert to complex
k = 6
print(complex(b,k))

#d) boolean(they are placed in numeric because true is 1 and false is 0)
t = b<k
print(t)
f = b>k
print(f)
#boolean convert to int.
print(int(t))
print(int(f))


# ----------------------------------------------------------------------------------------------- #
# 3) Sequence
			#list
			#set
			#tuple
			#string
			#range
# a)List
lst = [23,54,23,12,33]
print(type(lst))

# b)Set (No duplicate item)
s = {12, 24, 12, 12, 1}
print(type(s))

# c)Tuple (Immutable i.e not changed hence retrieving and iterating is fast)
t = (25,36,4,57,12)
print(type(t))

# d)String (Python dpnt have char type like in Java, C etc)
str = "Nisum"
st = "a"  #(for char)
print(type(st))

# e)Range
#define range(10)
#convert the range into list
print(list(range(10)))
#List of odd no starting from 3 end on 9
print(list(range(3,9,2)))

# ----------------------------------------------------------------------------------------------- #
# 4) Dictionary (key, value) for e.g rollno, studentname (key must be unique)
d = {'01':'Ali', '02':'Ahmed', '03':'Zubair'}
print(d)
print(d.keys()) #To print all the keys we have keys() builtin func
print(d.values()) #To print all the values we have values() builtin func
#To find the value for particular we have following ways. 
print(d['01'])
print(d.get('01')) 
#To check that particular key exist
print(d.has_key('01')) 
