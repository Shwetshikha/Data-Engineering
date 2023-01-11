import os
# 1. Accept number from the user

num1 = int(input("Enter first number "))
num2 = int(input("Enter second number "))
res = num1 + num2
print("Sum of two number is ", res)

# 2. Display three string "Name", "is, "James as "Name is James"

print("My", 'Name', "is", "James", sep="**")

# 3. Convert decimal number into octal using print() output formatting
num = 13
print('%o' % num)

# 4. Display float number with 2 decimal places using print()
num = 567.56999
print('%.3f' % num)

# 5. Except a list of 5 float numbers as an input from the user
# numbers = []
# for i in range(0,5):
#     print("Enter number at location", i, ":")
#     item = float(input())
#     numbers.append(item)
# print("List of Float numbers: ", numbers)

# 6. Write all content of a given file into a new file by skipping line number 5
with open("test.txt", "r") as fp:
    lines = fp.readlines()
with open("new_file.txt", "w") as fp:
    count = 0
    for line in lines:
        if count == 4:
            count += 1
            continue
        else:
            fp.write(line)
        count += 1
print("Done adding lines to new file")

# 7. Accept any three string from one input() call
str1, str2, str3 = input("Enter three string").split()
print("Name1", str1)
print("Name2", str2)
print("Name3", str3)

# 8. Format variables using a string.format() method
totalMoney = 1000
quantity = 3
price = 450
statement = "I have {1} dollars so that I can buy {0} football for {2} dollars"
print(statement.format(quantity, totalMoney, price))

# 9. Check file is empty or not
# import os
size = os.stat("new_file.txt").st_size
if size == 0:
    print("File is empty")
else:
    print("File not empty")
# Read line number 4 from a file
with open("test.txt", "r") as fp:
    lines = fp.readlines()
    print(lines[2])

