# Encapsulation in Python
# Bundling data and methods within a single unit
# Create an Employee class by defining employee attribute such as name and salary as an instance variable and implementing behavior using work() and show() instance methods

class Employee:
    def __init__(self, name, salary, project, place):
        self.name = name
        self.__salary = salary
        self.project = project
        self.place = place
    # method -- to display employee details

    def show(self):
        # accessing public data member
        print("Name:", self.name, 'Salary:', self.__salary)

    def work(self):
        print(self.name, 'is working on', self.project)

    def details(self):
        print(self.name, 'is working on', self.project, 'drawing a total salary of', self.__salary, 'belongs to', self.place)
    # Creating an object of a class
emp = Employee('Shwet', 30000, 'Data', 'Delhi')

# Calling public method of the class
emp.work()
emp.show()
emp.details()
# Access Modifiers in python
# Three type of Modifiers are there -- 1. Public, 2. Private, 3. Protected
# self.name = name -- Public Member
# self._project = project -- Protected Member
# self.__project = project -- private member
# Data hiding using Encapsulation

# Public member
# Public data members are accessible within and outside of a class.
# Private Member
emp.show()
print('Salary:', emp._Employee__salary)

# Getters and Setters in python
# Getters -- To access data members
# Setters -- To modify the data members
# The primary source of using getters and setters is to ensure data encapsulation.

class Student:
    def __init__(self, name, age):
        # Private Menber
        self.name = name
        self.__age = age

    # getter method
    def get_age(self):
        return self.__age

    # setter Method
    def set_age(self, age):
        self.__age = age

stud = Student('Shwet', 25)

# retrieving age using getter
print('Name:', stud.name, stud.get_age())

# Change age using setter
stud.set_age(16)

# retrieving age using getter
print('Name:', stud.name, stud.get_age())
# Advantages of Encapsulation -- Security, data hiding, simplicity, aesthetics
# Constructor in Python -- optional -- every class in python has a constructor but it is nor required to define it.
# Polymorphism
class Circle:
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        print("Area of circle :", self.pi * self.radius * self.radius)

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calculate_area(self):
        print("Area of Rectangle :", self.length * self.width)

# function

def area(shape):
    # Call Action
    shape.calculate_area()

cir = Circle(5)
rect = Rectangle(10, 5)

area(cir)
area(rect)
