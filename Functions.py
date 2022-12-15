# WRITING FUNCTIONS
# break down the code into number of functions so as to ease out code
# "def" is the short word for "define" then give the name for function , underscore for separating words then ()

def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome to the 'Functions'!")


greet("Shwet", "Shikha")
greet("Shikha", "SDE 1")
greet("Python", "Programming")


# difference between greet function and print function
# Arguments
# TYPES OF FUNCTIONS
def get_greeting(name):
    return f"Hi {name}"


get_greeting("Shikha")
message = get_greeting("Shwet")
print(message)


# KEYWORD ARGUMENT
def increment(number, by):
    return number + by


print(increment(2, by=3))


# DEFAULT ARGUMENT

def increase(number, by=4):
    return number + by


print(increase(2, 5))
print(increase(2))

# X-ARGUMENT
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))

# XX-ARGUMENTS 7 Lecture
def save_user(**user):
    print(user)

save_user(id = 1, name = 'Shwet', age=22)

print(type(save_user))

