# Built-in Data Structures in Python
# LIST[], SETS{}, TUPLE(), DICTIONARY {} -- Data Type
# objects- string, integer, boolean
# list - to define a sequence of objects
letters = ["a", "b", "c"]
# Creating a 2-dimensional list
matrix = [[0, 1], [2, 3], (1, 2), {1, 2}]
zeros = [0] * 5
print(type(matrix[3]))
combined = zeros + letters
print(combined)
numbers = list(range(20))
print(numbers)
# 20 is not included in the range
num = list(range(20, 40))
numb_step = list(range(20, 40, 2))
print(num)
print(numb_step)

# increment a function by 4
for i in range(0, 20, 4):
    print(i, end=" ")
print()

# printing python range with negative step
# increment a function by -2
for i in range(25, 2, -2):
    print(i, end=" ")
print()
# using a float number
# for i in range(float(3.3)):
#     print(i)
# we get a type error : Float object cannot be interpreted as an integer
# Import numpy to get the result

chars = list("Hello World")
print(chars)
print(len(chars))

from itertools import chain

# Using chain method
print("Concatenating the result")
res = chain(range(5), range(10, 20, 2))

for i in res:
    print(i, end=" ")

# Accessing Items
numbers = list(range(20))
print(numbers[::2])
print(numbers[::-1])
print(numbers[::5])
design = (list(range(5)), list(range(4)))
print(design)

# List Unpacking
numbers = [1, 2, 3, 4, 5, 6]
first, second, *other = numbers
print(first)  # Unpacking
print(other)  # Packing
first, *other, last = numbers
print(first, last)
print(other)

# Looping over Lists
# Use of "enumerate"
letters = ["a", "b", "c", "d", 9, 8]
items = (0, "a")
index, letter = items
for index, letter in enumerate(letters):
    print(index, letter)
    print(letters)

# Adding or Removing items
letters = ["a", "b", "c", "d"]
letters.append("u")
print(letters)
letters.insert(0, "-")
print(letters)

# Remove
letters.pop(0)
print(letters)
letters.remove("b")
print(letters)
del letters[0:3]
print(letters)
letters.clear()
print(letters)

# Finding Items
letters = ["a", "b", "c", "", "a"]
print(letters.index("b"))
print(len(letters))
if "d" in letters:
    print(letters.index("d"))
else:
    print("No 'd' in letters")

# Count - Number of occurence of a particular item in the list
print(letters.count("d"))
print(letters.count("a"))
print(letters.index("a"))

numbers = [3, 52, 67, 89, 67, 45, 64, 100, 0, 3]
# numbers.sort()
print(sorted(numbers))
print(numbers)
numbers.sort(reverse=True)
print(numbers)
numbers.sort()
print(numbers)

# For Tuple
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("product3", 14)
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)

# Lambda function
items = [
    ("Product-A", 24),
    ("Product-B", 45),
    ("Product-C", 100),
    ("Product-D", 89)
]
items.sort(key=lambda item: item[1])
print(items)

# Map Function
prices = []  # Define an empty list
for item in items:
    prices.append(item[1])

print(prices)
# By using Map function
x = list(map(lambda item: item[1], items))
print(x)

# Filter Function
# Using the built-in function filter()
x = list(filter(lambda item: item[0] >= "Product-B", items))
print(x)
y = list(filter(lambda item: item[1] >= 50, items))
print(y)

# List Comprehensions
# [expression for item in items] -- shorter and cleaner code for mapping and filtering is by use of List Comprehensions
filtered = list(filter(lambda item: item[1] >= 40, items))
print(filtered)

# With list comprehensions

filter_comp = [item for item in items if item[1] >= 40]
print(filter_comp)

# Zip function
list1 = [1, 2, 3]
list2 = [10, 20, 30]

print(list(zip(list1, list2)))
print(list(zip("abc", list1, list2, "bcd")))

# Stacks
# Last in - First Out (LIFO)
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
browsing_session.append(4)
print(browsing_session)
last = browsing_session.pop()
print(last)
print(browsing_session)
print("redirect", browsing_session.pop())
print(browsing_session)
if not browsing_session:
    print("disable")
print(browsing_session[-1])

# Queues
# FIFO behaviour First in first out
# Module - say is a collection of  reusable codes
from collections import deque

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)
queue.popleft()
print(queue)
if not queue:
    print("empty")

# Tuples
point = 1, 2
print(type(point))
point = 1
print(type(point))
point = 1,
print(type(point))
point = (1, 2) + (3, 4)
print(point)
point = tuple([1, 2, "shwet"])
print(point)
print(point[1])
print(type(point[2]))
point = (1, 2, 3, 10)
print(point[0:2])
x, y, z, a = point
if 10 in point:
    print("exists")
# unpacking should contain same number of objects or it should be *other in place of y,z,a in example given
x, *y = point
print(point[2])

# Swapping Variables
x = 10
y = 11

z = x
x = y
y = z

print("x ", x)
print("y ", y)

# Or we can write this as below for shorter code in Python
x = 15
y = 20

x, y = y, x

print("x ", x)
print("y ", y)

from array import array

# ARRAYS IN PYTHON
# Array -- large sequence or list of numbers
# Typecode-- assigned, unassigned
# Typecode-- are the type of strings of one character that determines the type of object an array takes.
numbers = array("I", [1, 2, 3])
numbers[0] = 98
print(numbers)
numbers = [1, 2, 4, 5, 1, 3, 4, 5, ]
first = set(numbers)
print(type(first))
second = {1, 5}
union = first | second
print(union)
intersection = first & second
print(intersection)
difference = first - second
print(difference)
sematic_difference = first ^ second
print(sematic_difference)
if 1 in first:
    print("Yes, Number is present in the set")
else:
    print("Number doesn't exist in the set")
# No indexing in the set is possible as it is unordered collection of unique items

# Dictionaries
point = {"x": 1, "y": 2}
print(point)
point = dict(x=18, y=2)
print(point)
# both are correct ways of writing dictionary but second one is better
point["x"] = 10
point["z"] = 20
print(point)

if "a" in point:
    print(point["a"])
print(point.get("a", 0))
del point["x"]
print(point)
for key in point:
    print(key, point[key])

# Dictionary Comprehension
values = []
for x in range(5):
    values.append(x * 2)
values = {x: x * 2 for x in range(5)}
print(values)

# GENERATOR EXPRESSION
from sys import getsizeof
values = (x * 2 for x in range(100000))
print("gen:", getsizeof(values))
values = [x * 2 for x in range(100000)]
print("list:", getsizeof(values))

# Unpacking Operator
numbers = [1, 2, 3]
print(*numbers)
print(1, 2, 3)
values = list(range(5))
values = [*range(5), *"Hello"]
print(values)
first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 1 }
print(combined)

# EXERCISE - write a program to get the value of most repeating character in the sentence
from pprint import pprint
sentence = "This is a common interview question"
# let frequency be an empty dictionary
char_frequency = {}
print(type(char_frequency))
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
pprint(char_frequency, width=1)
char_frequency_sorted = sorted(char_frequency.items(), key=lambda kv: kv[1], reverse=True)
print(sorted(char_frequency.items(), key=lambda kv: kv[1], reverse=True))
print("The most repeated character is:")
print(char_frequency_sorted[0])
