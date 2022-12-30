# 1. Accept number from the user

# num1 = int(input("Enter first number "))
# num2 = int(input("Enter second number "))
# res = num1 + num2
# print("Sum of two number is ", res)

# 2. Display three string "Name", "is, "James as "Name is James"

# print("My", 'Name', "is", "James", sep="**")

# 3. Convert decimal number into octal using print() output formatting
num = 13
print('%o' % num)

# 4. Display float number with 2 decimal places using print()
num = 567.56999
print('%.3f' % num)

# 5. Except a list of 5 float numbers as an input from the user
numbers = []
for i in range(0,5):
    print("Enter number at location", i, ":")
    item = float(input())
    numbers.append(item)
print("List of Float numbers: ", numbers)

# 6. Write all content of a given file into a new file by skipping line number 5