students_count = 1000
print(students_count)
# primitive types can be numbers, boolean, float, strings etc

is_published = False
print(is_published)

# python is a case-sensitive language

course_name = "Python Programming"
print(type(course_name))
print(type(is_published))
print(type(students_count))

# Make sure that the variable names are meaningful and descriptive
# Snake case, Camel case, pascal case
print(len(course_name))
# print(len(is_published)) Boolean has no length
print(course_name[0])
print(course_name[-1])
print(course_name[0:4])
print(course_name[0:])
print(course_name[:3])

# ESCAPE SEQUENCE

course = "     Python \\Programming \n New Language"
print(course)

# Formatted String
first = "Shwet"
last = "Shikha"
full = f"{first} {last} {2 + 2}"
print(full)
print(len(full))

# STRING METHOD
course.upper()
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())
print(course.find("Pro"))
print(course.replace("P", "j"))
print("Pro" in course)
print("swift" not in course)

# Numbers
x = 1
x = 1.1
x = 1 + 2j
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)

x = 10
x = x + 3
x += 3
print(x)

# Working with Number
print(round(2.9))
print(abs(-2.9))

# Type Conversion
x = input("x:")
print(type(x))
y = int(x) + 1
print(y)
print(type(y))

# QUIZ
# Q1 What are the primitive types in python - int, str, num, bool,float
fruit = "Apple"
print(fruit[1])
# p
#
print(fruit[1:-1])
print(bool("False"))