import random
import math

print("This is the first code in python for snow Flakes")
print("*" * 10)
print("Hello World")
print(2 + 1)
print("After code Runner")
print("hello")
if 5 > 2:
    print("Five is greater than two!")
x = 5
y = "Hello World!"
x = "Sally"
print(x)
x = str(3)
y = int(3)
z = float(3)
print(type(x))
print(type(y))
print(type(z))
x = y = z = "orange"
print(x)
print(y)
print(z)
fruits = ["apple", "Banana", "Cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
x = "Python"
y = "is"
z = "New Language"
print(x + " " + y + " " + z)
# Global Variables Variables that are created outside of a function

x = "New Language"


def myfunc():
    print("Python is " + x)


myfunc()

# Global Keyword "To create a global variable inside a function, that variable is local, and can only be used inside that function
# To create a global variable inside a fiunction, you can use the word "global" as keyword"


def myfunc():
    global x
    x = "Awesome Language"


myfunc()
print("Python is " + x)

print(random.randrange(1, 20))
# Python casting
# Strings are Arrays
a = "Hello Python"
print(a[2])
print(len(a))
txt = "This course from W3 School is for free"
print("free" in txt)
print("shwet" in txt)
if "free" in txt:
    print("yes, 'free' is present in the text")
b = "Hello, World!"
print(b[2:9])
print(b[:5])
print(b[2:])
print(b[-5:-2])
print(b.replace("H", "J"))
print(a.split(","))
tax = 12.5/100
price = 100.50
amount = price * tax
print(amount)
for x in range(1, 5):
    print(x)
# use of parentheses is important in python 3
print(type('default string '))
print(type(b'string with b '))
try:
    trying_to_check_error
except NameError as err:
 print (err, 'Error Caused')
 x = ("apple", "banana", "cherry")
 print(type(x))
x = memoryview(bytes(5))
print(x)
print(type(x))
print(math.acos(-1))
x = 1
print(math.acos(x))

#In hyperbolic the value input has to be positive

print(math.acosh(7))
print(math.acosh(56))
print(math.acosh(2.45))
print(math.acosh(1))
# Number must lie between -1 to 1
print(math.asin(-1))
# arc tangent of a number in radians
print((math.atan(1)) * (180/3.14))
# arc tangent of y/x in radians
print(math.atan2(8,5))

# ceil For rounding off a number to nearest integer upper
print(math.ceil(3.6))
print(math.ceil(-6.8))
# floor for rounding off to nearest integer down
print(math.floor(7.8))
# comb in python
n = 7
k = 5
print(math.comb(n,k))
print(math.copysign(n,k))
print(math.copysign(-43, -78))
print(math.copysign(-73, 68.56))
print (math.cos(0.00))
print (math.cos(-1.23))
print (math.cos(10))
print (math.cos(3.14159265359))

#print distance between two points
p = [3]
q = [1]
print(math.dist(p,q))
p = [3, 3]
q = [6, 12]
#to calculate distance between two points with coordinates (x1, y1) and (x2, y2)
# use python command math.dist(p,q)
print(math.dist(p,q))