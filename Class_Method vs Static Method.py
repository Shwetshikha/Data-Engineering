import inspect

# Instance method -- performs a set of action on the data/ value provided bu the instance variable
# Class method -- is method that is called on the class itself, not on a specific object instance
# Static Method -- is a general utility method that performs task in isolation
class Student:
    # class variable
    school_name = "PPS School"

    def __init__(self, name, age):
        # Instance Variables
        self.name = name
        self.age = age

    # instance variables
    def show(self):
        print(self.name, self.age, Student.school_name)
    @classmethod
    def change_School(cls, name):
        cls.school_name = name
    @staticmethod
    def find_notes(subject_name):
        return ['chapter 1', 'chapter 2', 'chapter 3']
shwet = Student('Shwet', 25)
shwet.show()
Student.change_School('PPS School')
shwet.change_School('PQR School')
Student.find_notes('Math')
shwet.find_notes('Math')


# Object Introspection
# "dir" It is one of the important functions for introspection. It return a list of attributes and methods belonging to an object
my_list = [1,2,3,4]
print(dir())
# dir() will return all the names in the current scope
print(type(""))
print(type([]))
print(type({}))
print(type(dict))
print(type(5))
name = "Shwet"
print(id(name))
# Inspect Module
print(inspect.getmembers(str))

