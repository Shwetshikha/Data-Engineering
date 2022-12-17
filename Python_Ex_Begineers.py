# Calculate the multiplication and sum of two numbers
# given two integer number return their product only if the product is equal to or lower than 1000 else return sum
number1 = 20
number2 = 3
# Expected output 600
sum = int(number1 + number2)
product = int(number1 * number2)
if product <= 1000:
    print(product)
else:
    print(sum)

# Now by defining python function
def product_or_sum(num1, num2):
    # calculate the product
    product = num1 * num2
    sum = num1 + num2
    if product <= 1000:
        return product
    else:
        return sum


result = product_or_sum(20, 30)
print("The result is ", result)

result = product_or_sum(40, 40)
print("the result is ", result)

# Print the sum of current number and the previous number
# write the program to iterate first 10 numbers and in each iteration print the sum of current and previous number
previous_number = 0
for i in range(1, 21):
    sum = previous_number + i
    print("Current Number ", i, "Previous Number ", previous_number, "Sum", sum )
    previous_number = i

# Print Characters from a string that are present at an even index number
str = input("Enter Word ")
print("Original String: ", str)
length = len(str)
# print(str)
# print(length)
print("Printing only even index characters")
for i in range(0, length -1, 2):
    print("index[", i, "]", str[i])
print("printing only odd index chatacters")
for i in range(1, length - 1, 2):
    print("index[", i, "]", str[i])

# use List slicing for the same problem
word = input("Enter word to print desired index")
print("Original String :", word)
x = list(word)
print(x)
for i in x[0::2]:
    print([i], i)
for i in x[1::2]:
    print([i], i)


# Remove first n characters from a string
# String Slicing
def remove_char(word, n):
    print("Original String:", word)
    x = word[:n]
    return x

print("Removing Characters from a string")
print(remove_char("Pynative", 4))
print(remove_char("pynative", 2))

# Check if the first and last number of a list is the same

def check_num(numberlist):
    print("Given List: ", numberlist)

    first_num = numberlist[0]
    last_num = numberlist[-1]

    if first_num == last_num:
        return True
    else:
        return False

numberlist_x = [10, 20, 30, 50, 10]
print("result is", check_num(numberlist_x))
numberlist_y= [20,20, 89, 90]
print("result is",check_num(numberlist_y))

# Display numbers divisible from a list
def divisible(numberlist):
    print("The original List of Numbers is: ", numberlist)
    print("The number divisible by 5 are: ")
    for i in numberlist:
        if i % 5 == 0:
            print(i)
        else:
            i = i +1


numberlist_x = [10, 24, 56, 90, 65]
divisible(numberlist_x)

# Return the count of a given substring from a string
str_x = "Shwet is a developer. Shwet is a writer"
str = "Shwet"
if str in str_x:
    print("Shwet appeared", str_x.count(str), "times in the string")

# By defining a function
def count_shwet(statement):
    print("Given String: ", statement)
    count = 0
    for i in range(len(statement) - 1):
        count += statement[i: i + 4] == 'Shwet'
    return count

count = count_shwet("Shwet is a developer. Shwet is a writer. Shwet stays in Delhi")
print("Shwet appeared ", count, "times")

# Print the following pattern

for x in range(6):
    for i in range(x):
        print(x, end=" ")
    print("\n")

# Check palindrome Number
# write a program to check if the given number is a palindrome number

def palindrome(num):
    print("This is original number: ", num)
    rev_num = 0
    original_num = num
    while num > 0:
        reminder = num % 10
        rev_num = (rev_num * 10) + reminder
        num = num // 10

    if original_num == rev_num:
        print("Given number is a palindrome")
    else:
        print("Given number is not palindrome")

palindrome(int(input("Input the number to be checked for palindrome:  ")))

# Create a new list from a two list using the following condition
# Given two list of numbers write a program to create a new list such that it contain odd number from first list and even number grom second list

list1 = [10, 45, 50, 56, 33, 78, 89]
list2 = [9, 45, 88, 90, 63, 22, 90]
even = []
odd = []
# result = even + odd
for i in list1:
    if i % 2 != 0:
        odd.append(i)
for i in list2:
    if i % 2 == 0:
        even.append(i)

result = odd + even
print("This is the list containing odd number from list1 and even number from list2 :", result)

# Write a program to extract each digit from an integer in the reverse order
def reverse(num):
    print("Given Number: ", num)
    while num > 0:
        digit = num % 10
        num = num // 10
        print(digit, end= " ")


reverse(int(input("Input number to get the reverse order")))



