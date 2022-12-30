# Print 10 natural numbers using while loop
i = 1
while i <= 10:
    print(i)
    i += 1

# Print the pattern
rows = 5
for i in range(1,rows + 1, 1):
    for j in range(1, i+ 1):
        print(j, end=" ")
    print(" ")

row = int(input("The number of rows for which you want to print the pattern"))
for i in range(1, row + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print(" ")

# Calculate the sum of all numbers from 1 to a given number
num = int(input("Input number to get the sum"))
print("The number input is", num)
sum = 0
for i in range(0, num + 1):
    current = i + sum
    sum = current
    avg = sum // num
print("The sum of all numbers from 1 to ", num,"is : ", sum)
# Calculate the sum and average in python
print("The average of all numbers from 1 to ", num,"is : ", avg)

# Write a program to print multiplication table of a given number
num = int(input("Enter the number to print the table"))
for i in range(1, 10 + 1):
    p = i * num
    print("The multiplication of", num, "*", i, "is: ", p)
print("")
# Display numbers from a list using loop
number = [12, 75, 150, 180, 145, 525, 50]
for i in number:
    if i > 500:
        break
    elif i > 150:
        continue
    elif i % 5 == 0:
        print(i)
# Count the total number of digits in a number
num = int(input("Enter number to count the digits"))
count = 0
while num != 0:
    num = num // 10
    count += 1
print("Total digits are: ", count)

# print the pattern
n = 6
k = 5
for i in range(0, n + 1):
    for j in range(k-i,0, -1):
        print(j, end=" ")
    print()
# Print list in reverse order using loop
list = [10, 20, 30, 40, 50, 60, 70]
reverse = reversed(list)
for item in reverse:
    print(item)
# Display numbers from -10 to -1 using for loop
for i in range(-10, 0, 1):
    print(i)
print("Done!")

