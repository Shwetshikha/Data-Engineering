# Scope
#Global variables are defined before defining a function but its value can be changed by defining them locally as shown below

message = "Global Variable"

def greet(name):
    # global message
    message = "a"
    print("Message for greet function: " + message)

def send_email(name):
    # global message
    # message = "b"
    print("Message for send_email function: " + message)


greet("Shwet")
send_email("Shikha")
print("This one is for printing Global variable: " + message)

# Que: why print statement 19 is not taking global variable assigned earlier ?

# Exercise -12 fizz- buzz problem
def fizz_buzz(input):

    if (input % 3 == 0) and (input % 5 == 0):
        return "Fizz Buzz"
    if input % 3 == 0:
        return "Fizz"
        # print("FIZZ")
    if input % 5 == 0:
        return "Buzz"
        # print("BUZZ")
        # print("FIZZ BUZZ")
    # else:
    #     print(input)
    return input


print(fizz_buzz(7))

# Shifting the and condition to up shows a more clear and logical code as if we input 15 it is divisible by 3 and 5 both hence will print the return values of all three conditions.
# alter the sequence of 26 and 27 to see the change.