# 1. Create a function in python
def short(name, department):
    print(name, department)

# Call the function
short("Shwet","Technical")
short("Manvi","Technical")

# 2. Create a function with variable length of arguments
def show_employee(name="Shikha", salary=20000):
    print("Name:", name, "salary:", salary)

show_employee("Shwet", 30000)
show_employee("Manvi")
show_employee("name", 40000)
show_employee()
# setting default argument to display the same if some argument is not given

# 3. Create an inner function to calculate the addition in the following way
def outer(a,b):
    print("outer function")
    square = a ** 2
    def addition(a,b):
        return a + b
    # calling the inner function from outer function
    add = addition(a,b)
    # add 5 to the result
    return add + 5

# calling outer function as a variable and passing the argument
result = outer(5, 10)
print(result)
# 6. Create a recursive function to calculate the sum of numbers from 0 to 10
def addition(num):
    if num:
        # call the same function by reducing number by 1
        return num + addition(num - 1)
    else:
        return 0
# res = addition(10)
res = addition(20)
print(res)

# 7. Assign a different name to function and call it through the new name

