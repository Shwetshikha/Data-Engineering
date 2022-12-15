x = bool(10 > 3)
print(x)
# Comparison Operator

x = bool(10 == 10)
print(x)
x = bool(10 == "10")
print(x)

# Conditional Statements
temperature = 60
if temperature > 33:
    print("It's Warm")
    print("Drink Water")
elif temperature > 32:
    print("It's nice")
else:
    print("It's Cold")
print("Done")

# Ternary Operator and writing clean codes
age = 22
message = "Eligible" if age >= 18 else "Not Eligible"
# if age >= 18:
#     message = "Eligible"
# else:
#     message = "Not Eligible"
print(message)

# Logical Operator
high_income = False
good_credit = False
student = False

# if high_income and good_credit:
#     print("Eligible")
# else:
#     print("Not Eligible")
# if not student:
#     print("Not a student")

if (high_income and good_credit) and not student:
    print("Eligible for Loan")
else:
    print("Not Eligible for loan")

# Short circuit Evaluation
# Chaining Comparison Operators

# age should be between 18 and 65
age = 22
if 18 <= age <65:
    print("Eligible as Adult")

# QUIZ
if 10 == "10":
    print("a")
elif "bag" > "apple" and "bag" > "cat":
    print("b")
else:
    print("c")
# Predicted output c
# 10 !== "10" because of string and integer
#  bag > apple true from sorting but bag < cat so the operator comes out of loop by setting it to false
# and hence the output should be the else statement that is print "c"


# LOOPS
print("Sending a message")
# For Loop
for number in range(3):
    print("Attempt", number + 1, (number + 1) * ".")
    print("Attempt", number, number * ".")

# For Else Loop
successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("successful")
        break
    else:
        print("Attempted 3 times and failed")
# Nested Loop
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")
for x in range(3):
    for y in range(3):
        for z in range(2):
            print(f"({x}, {y}, {z})")

# ITERABLES
print(type(5))
print(type(range(5)))
# we can iterate over it "range objects"
for x in "python":
    print(x)
    # print("\n")
for x in [1, 2, 3, 4, 5]:
    print(x)

# While Loop
number = 100
while number > 0:
    print(number)
    number = number // 2

command = ""
while command != "quit" and command != "QUIT":
    command = input(">")
    print("ECHO", command)
# INFINITE LOOPS
# while True:
#     command = input(">")
#     print("ECHO", command)
#     if command.lower() == "quit":
#         break

# EXERCISE
# PRINT EVEN NUMBERS BETWEEN 1 AND 10 AND TOTAL NUMBER OF EVEN NUMBER EXISTING
count = 0
for number in range(1, 20):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"We have total of {count} even numbers between 1 and 10")

# Print odd numbers between 1 to 10

count = 0
for number in range(1,20):
    if number % 2 == 1:
        count += 1
        print(number)
print(f"We have a total of {count} odd numbers between 1 to 10")

# Print numbers divisible by 5
count = 0
for number in range(1,100):
    if number % 5 == 0:
        count += 1
        print(number)
print(f"We have in total {count} numbers divisible by 5")

# print prime numbers between 1 and 10
for number in range(1,20):
    for i in range(2,number):
        if (number % i) == 0:
            print(number, "is not a prime number")
            print(i, "times", number//i, "is", number)
            break
    else:
        print(number,"is a prime number")

