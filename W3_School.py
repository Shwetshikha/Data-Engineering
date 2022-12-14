for x in "banana":
    print(x)
txt = "The best thing!"
print("expensive" not in txt)

# python - Slicing Strings
word = "Hello World!"
print(word[-5:-2])
name = "Shwet Shikha"
dept = "Tech"
number = 3
txt = "Myself {} from {} with RollNumber {}"
print(txt.format(name, dept, number))
x = 200
print(isinstance(x, str))
# Python List
thislist = ["Apple", "Banana", "cherry"]
thislist[1] = "Ice cream"
print(thislist)
thislist[1:2] = ["one", "two"]
print(thislist)
thislist.insert(2, "insert")
print(thislist)

# Adding items to list
thislist.append("Orange")
print(thislist)
thislist.insert(2, "pineapple")
nest = ["mango", "pine"]
thislist.extend(nest)
print(thislist)

# Remove items in list
thislist.remove("one")
print(thislist)
print(len(thislist))
thislist.pop(2)
print(thislist)
# Remove last item from list
thislist.pop()
print(thislist)
del thislist[0]
print(thislist)
thislist.clear()
print(len(thislist))

# PYTHON LOOP LIST#
thislist = ["apple", "cherry", "banana"]
for x in thislist:
    print(x)
for i in range(len(thislist)):
    print(thislist[i])
i = 0
while i < len(thislist):
    print(thislist[i])
    i += 1

# List Comprehension offers a shorter syntax when we want to create a new list based on the existing list
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)
newlist = [x.upper() for x in fruits]
print(newlist)
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

# Sorting of list
print(thislist)
newlist.sort()
print(newlist)
thislist = [100, 50, 65, 82, 23, 85]
thislist.sort()
print(thislist)
thislist.sort(reverse=True)
print(thislist)

# Customize sort function


def myfunc(n):
    return abs(n - 50)


thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)
thislist.extend(newlist)
print(thislist)

# Tuples
# To store multiple items in single variable "Collection that is orderd and unchangble"
thistuple = ("apple", "cherry", "cherry")

print(thistuple)
print(type(thistuple))
print(type(thislist))

# Tuples are unchangeble, you cannot add, remove items once tuple is created
# tuples are unchangeable, immutable
x = thistuple
print(x)
print(type(x))
y = list(x)
print(y)
print(type(y))

# UNPACKING A TUPLE
# When we create a tuple we normally assign a value to it, called "packing" a tuple.
# Extracting the values back into variables is called "unpacking"
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
# PYTHON SET
myset = {"apple", "banana", "cherry", "apple"}
print(myset)
print(len(myset))
set1 = {"apple", "Banana", "cherry"}
set2 = {1, 5, 7, 9, 0}
set3 = {True, False, False}
print(type(set1))

# set() constructor can also be used to make set
thisset = set(("apple", "banana", "pineapple"))
print(type(thisset))
# Python Access set Items
# cannot access items in a set by referring to an index or a key
# but can loop through the set items
for x in set1:
    print(x)
set1.add("orange")
print(set1)
tropical = {"pine", "mango"}
set1.update(tropical)
print(set1)
# removing set Items
set1.remove("pine")
print(set1)

# PYTHON - JOIN SETS
# union()
set4 = set1.union(set2)
print(set4)

print(set4)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

# Python Dictionaries
thisdict = {
    "brand": ("Ford"),
    "model": {"Mustang"},
    "year": 1964,
    "colors": ["red", "White", "blue"]
}
print(thisdict)
print(type(thisdict))
print(thisdict["brand"])
print(len(thisdict))
print(type(thisdict["colors"]))
print(type(thisdict["year"]))
print(type(thisdict["model"]))
print(type(thisdict["brand"]))

# Dictionary Items data type

# The Dictionary constructor
thisdict = dict(name="John", age=36, country="Norway")
print(thisdict)
x = thisdict.values()
print(x)
y = thisdict.keys()
print(y)

# Get Items
x = thisdict.items()
thisdict.popitem()
print(thisdict)
# thisdict.popitem()
# print(thisdict)
del thisdict["age"]
print(thisdict)

dict = {
    "brand": ("Ford"),
    "model": {"Mustang"},
    "year": 1964,
    "colors": ["red", "White", "blue"]
}
this = dict.copy()
print(this)

# Nested Dictionaries
# A dictionary can contain dictionaries called as nested dictionary
child1 = {
    "name": "Shwet",
    "year": 2022
}
child2 = {
    "name": "Shikha",
    "year": 2021
}
child3 = {
    "name": "Toshi",
    "year": 2020
}

myfamily = {
    "Myself": child1,
    "sibling": child2,
    "sibling2": child3
}
print(myfamily)
print(type(myfamily))
