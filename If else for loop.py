# # Print  natural numbers
# i= int(input("Enter the number to print"))
# for i in range(1, i):
#     print(i)
#     i = i + 1
#
# # print the pattern
# pattern = int(input("Enter the rows you want to print the pattern for"))
# for i in range(1,pattern + 1):
#     for j in range(1, i+1):
#         print(j, end=' ')
#     print("")
# # calculate the sum of all numbers from 1 to a given number
# input = int(input("Enter the number to find the sum"))
# sum = 0
# for i in range(1, input + 1):
#     sum = sum + i
# print("The sum is :", sum)
#
# # Write a program to print multiplication table of a given number
# n = 2
# for i in range(1, 11, 1):
#     product = n * i
#     print(product)
#
# # Display numbers from a list using loop
# # Conditions --The number must be divisible by five
# # If the number is greater than 150, then skip it and move to the next number
# # If the number is greater than 500, then stop the loop
# numbers = [12, 75, 150, 180, 145, 890, 43]
# for i in numbers:
#     if i > 500:
#         break
#     elif i > 150:
#         continue
#     elif i % 5 == 0:
#         print("The number divisible by 5 but less than 500: ", i)

# count the total number of digits in a number
# number = int(input("Enter the number to print"))
# count = 0
# while number != 0:
#     number = number // 10
#     count += 1
# print("Total digits are: ", count)
# Print the pattern
# rows = int(input("Enter the number of rows you want to print the pattern for"))
rows = 5
column = 5
for i in range(0, rows + 1):
    for j in range((column - i),0,-1):
        print(j,end=' ')
    print()
n = 5
k = 5
for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j,end=' ')
    print()

# Print list in reverse order
list1 = [10, 20, 30, 40, 50]
new_list = reversed(list1)
for i in new_list:
    print(i)

# Display numbers from -10 to -1 using loop
for i in range(-10, 0, 1):
    print(i)
# use else block to display a message "Done" after successful execution of for loop
for i in range(5):
    print(i + 1)
else:
    print("Done")

# Write a program to display all prime numbers within a range
start = int(input("Enter start number"))
end = int(input("Enter the end number to find the prime number"))
print("The prime number between", start, "and", end, "are: ")
for num in range(start, end+ 1, 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)

# Display Fibonacci series upto 10 terms
num1 = 0
num2 = 1
num = int(input("Enter the number for fibonacci series"))
print("Fibonacci Seq")
for i in range(num + 1):
    print(num1, end=" ")
    res = num1 + num2
    num1 = num2
    num2 = res

# find the factorial of a given number
number_factorial = int(input("Enter number to find factorial"))
fac = 1
if num < 0:
    print("Factorial for negative number doesn't exist")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, number_factorial + 1):
        fac = fac * i
    print("The factorial of", number_factorial, "is", fac)

# Reverse a given integer number
integer = int(input("Enter the integer to find the reverse oder"))
reverse_integer = 0
print("The given number", integer)
while integer > 0:
    reminder = integer % 10
    reverse_integer = (reverse_integer * 10) + reminder
    integer = integer // 10
print("Reverse Integer ", reverse_integer)

# Use Loop to display elements from a given list present at odd index position
list = [1, 3, 4, 5,6, 78, 56, 7]
for i in list[1::2]:
    print(i, end=" ")
# calculate the cube of all numbers from 1 to a given number
cube = int(input("Enter range for which you want to print the cube"))
for i in range(1, cube+1):
    cu = i ** 3
    print("The cube of current number", i,"is", cu)
print(" ")
# Find the sum of the series upto n terms
# number of terms
n = 5
start = 2
sum_seq = 0
for i in range(0, n):
    print(start, end="+")
    sum_seq += start
    start = start * 10 + 2
print("\nSum of above series is:", sum_seq)

# Print the following pattern
rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=" ")
    print("\r")
for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")