# create a class with instance atrribute
# write a python program to create a vehicle class with max_speed and mileage
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
modelX = Vehicle(240, 18)
print(modelX.max_speed, modelX.mileage)
# create a vehicle class without any variables and method
class Vehicle:
    pass
# Create a child class bus that will inherit all of the variables and methods of vehicle class
# Given
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

# Create a Bus object that will inherit all of the variables and methods of the parent Vehicle class and display it
class Bus(Vehicle):
    pass
school_bus = Bus("School Volvo", 180, 12)
print("Vehicle.name:", school_bus.name, "Speed:", school_bus.max_speed, "Mileage:", school_bus.mileage)

# Class Inheritance
# Create a Bus class that inherit from the vehicle class, Give the capcity argument of Bus.seating_capacity() a default value of 50
#
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The Seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)
School_bus = Bus("school Benz", 170, 12)
print(School_bus.seating_capacity())

# Define a property that must have the same value for every class instance(object)
# Define a class attribute 'color' with a default value white i.e Every Vehicle should be white
class Vehicle:
    color = "White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

car = Car("Audi Q5", 240, 18)
print(car.color, car.name, "Speed:", car.max_speed, "Mileage:", car.mileage)

# Class Inheritance
# Create a Bus child class that inherits from the vehicle class. The default fare charge of any vehicle is seating capacity * 100.
# If the vehicle Bus instance, we need to add an extra 10% on full fare as maintenance charges. so that total fare for bus instance will become the final amount = tt fare + 10% total fare
class Vehicle:
    def __init__(self, name, max_speed, mileage, capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        amount = super().fare()
        amount += amount * 10/100
        return amount

School_bus = Bus("School car", 12, 340, 50)
print("Total bus fare is:", School_bus.fare())

# Check type of an object
# write a program to determine which class a given Bus object belongs to
print(type(School_bus))
print(type(Vehicle))

# Determine if School_bus is also an instance of the Vehicle class
print(isinstance(School_bus, Vehicle))
print(isinstance(Bus, Vehicle))
print(isinstance(School_bus, Bus))
# OOPS

class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram
        print("in init")

    def config(self):
        print("config.is", self.cpu, self.ram)

com1 = Computer(15, 16)
com2 = Computer('Ryzen 3', 8)
print(type(com1))
# Class.method(object) -- for which you want an output
Computer.config(com1)
Computer.config(com2)
com1.config()

# Inner Class in Python
class Student:              # Outer class

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.laptop()

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class laptop:

        def __init__(self):
            self.brand = "Hp"
            self.cpu = "i5"
            self.ram = 8
        def show(self):
            print(self.brand, self.cpu, self.ram)

s1 = Student('Shwet', 1)
s2 = Student('Shikha', 2)

s1.show()
print(s1.lap.brand)
# Inheritance
class A:
    def feature1(self):
        print("Feature 1 Working")
    def feature2(self):
        print("Feature 2 Working")

class B(A):             # Child class of A
    def feature3(self):
        print("Feature 3 Working")
    def feature4(self):
        print("Feature 4 Working")

class C(B):
    def feature5(self):
        print("Feature 5 Working")
    def feature6(self):
        print("Feature 6 Working")
a1 = A()

a1.feature1()
a1.feature2()

b1 = B()
b1.feature4()
c1 = C()
c1.feature1()

# Polymorphism
class PyCharm:
    def execute(self):
        print("compiling")
        print("running")

class laptop:
    def code(self, ide):
        ide.execute()

ide = PyCharm()
lap1 = laptop()
lap1.code(ide)
