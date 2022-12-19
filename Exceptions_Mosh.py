# There occur many type of error
# Example : Type Error, I
# number = [1, 2]
# print(number[3])

# We get an error -- Index type i.e list index out of range
# Handling Error
# Handling Different Exceptions
# Cleaning Up
# The With statement
try:
    with open("Exceptions_Mosh.py") as file, open("W3_School.py") as target:
        print("File is opened")
    # file = open("Exceptions_Mosh.py")
    age = int(input("Age: "))
    xfactor = 10 / age
    # file.close()
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age")
    # print(ex)
    # print(type(ex))
except ZeroDivisionError:
    print("Age cannot be 0")
else:
    print("Excecution continues.")
finally:
    file.close()

# Raising Exceptions
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less")
    return 10 / age
try:
    calculate_xfactor(10)
except ValueError as error:
    print(error)
# Cost of Raising Exceptions
from timeit import timeit

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less")
    return 10 / age
try:
    calculate_xfactor(10)
except ValueError as error:
    print(error)
"""
print("First Code", timeit(code1, number=10000))