# Object-oriented Programming in Python
# Procedural Programming
# set of Steps, in the form of functions and code-blocks, that flow sequentially in order to complete a task
# Not only data but overall structure of program is written in the form of Object
# Classes are used to create user-defined data structures.
# Classes define functions called methods, which identify the behaviour and actions that an object created from the class can perform with its data.
# Defining a class
# class Dog:
#     species = "Canis familiaris"
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# Classes -- in built classes (int, bool etc)-- methods are already defined
# Customised classes --

from abc import ABC, abstractmethod
from collections import namedtuple

numbers = [1,2]


# define a class
class Point:
    default_color = "red"

    def draw(self):          # define the function(parameter-- 'self')
        print("Draw")

    # Defining a class
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod            #decorators: to extend the behavior of class or method
    def zero(cls):
        return cls(0, 0)


    def draw(self):
        print(f"Point ({self.x}, {self.y}")

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

point = Point(1,2)             # Creating a point object by calling as function.
print(type(point))          # In the output we get '__main__.Point' where main is the name of module
print(isinstance(point, Point))  # If we need to know the object is an instance of the defined class -- here 'point' is an object of class 'Point' hence it returns true
print(isinstance(point, int))   # here it returns false as point is not an instance of class integer

# Constructors
point = Point(1,2)  # takes 2 argument
point.draw()    # takes only one argument self by default

# Classes v/s Instance Attributes
point = Point(3,7)
point.draw()
another = Point(7,8)
another.draw()
print(another.default_color)
point.default_color = "yellow"
print(point.default_color)

# Classes v/s Instance Methods

point = Point.zero()
print(point)
print(Point.zero())

# Magic Methods and Inheritance
point = Point(8,9)
print(str(point))
# Comparing objects
point = Point(6,7)
other = Point(6, 9)
print(point == other)
point = Point(4,1)
other = Point(5,16)
print(point < other)

# Performing Arithmetic Operations
point = Point(10,20)
other = Point(5, 6)
combined = point + other
print(combined.x)
print(combined)
# Making Custom Containers
class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        # self.tags[tag] = self.tags.get(tag, 0) + 1
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)

cloud = TagCloud()
cloud["python"] = 10
cloud.add("Python")
cloud.add("PYTHON PROGRAMMING")
cloud.add("python")
cloud.add("python")
cloud.add("python")
cloud.add("python")
print(cloud.tags)
print(cloud["PYTHON"])

# private Members
# Properties
class Product:
    def __init__(self, price):
        self.set_price(price)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price Cannot be NEGATIVE")
        self.__price = value

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value

    price = property(get_price, set_price)

product = Product(50)
product.price = 5
print(product.price)

# Inheritance
class Animal(object):
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")

# Animal: Parent, Base class
# Mammal: Child, Sub
#
class Animal():
    def __init__(self):
        print("Animal Constructor")
        self.age = 1

    def eat(self):
        print("eat")

class Mammal(Animal):
    # def eat(self):
    #     print("eat")
    def __init__(self):

        print("Mammal Constructor")
        self.weight = 2
        super().__init__()

    def walk(self):
        print("Walk")



class Fish(Animal):
    # def eat(self):
    #     print("eat")

    def swim(self):
        print("Swim")

m = Mammal()
m.eat()
# print(m.age)

# The object class
print(isinstance(m, object))
print(issubclass(Mammal, object))
print(issubclass(Mammal, Animal))

# Method Overriding

print(m.age)
print(m.weight)

# Multi-level Inheritance
# Inheritance abuse

class Animal():
    def eat(self):
        print("eat")

class Bird(Animal):
    def fly(self):
        print("fly")

class Chicken(Bird):
    pass

print(Bird())

# Multiple Inheritance
class Employee:
    def greet(self):
        print("Employee Greet")


class Person:
    def greet(self):
        # print("Person Greet")
        pass

class Manager(Employee, Person):
    pass

manager = Manager()
employee = Employee()
person = Person()
employee.greet()
manager.greet()
person.greet()

# Inheritance Example
# ABC --- Abstract Base Class

class InvalidOperationError(Exception):
    pass

class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already opened")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False

    @abstractmethod
    def read(self):
        pass

class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a Network")

# Abstract Base Classes
# from abc import ABC, abstractmethod
class MemoryStream(Stream):
    def read(self):
        print("Reading data from a memory stream")

stream = MemoryStream()
stream.open()

# Polymorphism
class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass

class TextBox(UIControl):
    def draw(self):
        print("TextBox")

class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")

def draw(control):
    control.draw()
ddl = DropDownList()
textbox = TextBox()
draw(textbox)
draw(ddl)

print(isinstance(ddl, UIControl))
print(isinstance(textbox, UIControl))

# Inheritance with Built-in Types
class Text(str):
    def duplicate(self):
        return self + " " + self

class TrackableList(list):
    def append(self, object):
        print("Append called")
        super().append(object)

list = TrackableList()
list.append("1")
text = Text("Python")
print(text.lower())
print(text.duplicate())

# Data Classes
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
p2 = Point(1, 2)
# since Tuple are immutable hence we can't change them
# p1.x = 10 -- will give Attribute Error
p1 = Point(x= 10, y=2)
print(id(p1))
print(id(p2))
print(p1 == p2)