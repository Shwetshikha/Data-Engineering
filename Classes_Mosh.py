# Classes in Python
numbers = [1,2]
print(type(numbers))

# How to create  custom classes:
# Class: Blueprint for creating new objects
# Object: instance of a class

# Class: Human
# Objects: Shwet, Manvi
# creating classes in python
class Point:
    def draw(self):
        print("draw")
point = Point()
print(type(point))
print(type(Point))
print(isinstance(point, Point))
print(isinstance(point, int))

# Constructors
# For creating a new point object
class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def Zero(cls):
        return cls(0, 0)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def draw(self):
        print(f"Point ({self.x}, {self.y})")

point = Point(1, 2)
another = Point(5, 6)
point.default_color = "Yellow"
print(point.default_color)
print(point.default_color)
print(point.x)
print(point.y)
point.draw()
another.draw()

# Class vs Instance Methods

point = Point.Zero()
point.draw()

# Magic Methods
point.__str__()

# Comparing Objects
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


point = Point(10, 20)
other = Point(1, 2)
print(point < other)

# Performing Arithmetic Operations
combined = point + other
print(combined.x)
print(combined.y)

# Making Custom Containers
class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
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
len(cloud)
cloud.add("Python")
cloud.add("python")
cloud.add("python")
print(cloud.tags)
