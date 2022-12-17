# Exercise from Pynative
# Write a program to create a string made of the first, middle and last charachter

str1 = "James"
x = int(len(str1) / 2)
result = str1[0] + str1[x] + str1[-1]
print(result)

# Create a string made of middle three characters : Expected output = "Dip"
str1 = "JhonDipPeta"
middle = int(len(str1) / 2)
result = str1[middle -1] + str1[middle] + str1[middle + 1]
print(result)

# case 2 expected output: "Son"
str2 = "JaSonAyy"
middle = int((len(str2) - 1 ) / 2)
result = str2[middle -1] + str2[middle] + str2[middle +1]
print(result)
print(middle)

# Append new string in the middle of a given string
# Expected output: "AuKellylt"

s1 = "Ault"
s2 = "Kelly"
print(len(s1))
middle = int((len(s1))/ 2)
print(middle)
x = s1[:middle:]
x = x + s2
x = x + s1[middle:]
print(x)
# Create a new String made of first, middle and last characters of each input string
# Expected Output: "AJrpan"
s1 = "America"
s2 = "Japan"
firt_char = s1[0] + s2[0]
last_char = s1[-1] + s2[-1]
mi1 = int(len(s1) / 2)
mi2 = int(len(s2) / 2)
middle_char = s1[mi1] + s2[mi2]
print(s1[mi1])
print(s2[mi2])
result = firt_char + middle_char + last_char
print(result)

# Arrange string characters such that lowercase letters should come first
# Expected Output: "yaivePNT
str1 = "PyNaTive"
lower = []
upper = []
for ch in str1:
    if ch.islower():
        lower.append(ch)
    else:
        upper.append(ch)
sorted_str = ''.join(lower + upper)
print(sorted_str)

# Count all letters, digits and special symbols from a given string
# Expected Output: char= 8, Digits = 3, symbol=4
str1 = "P@#yn26at^&i5ve"
character = []
digits = []
symbol = []
for ch in str1:
    if ch.islower() or ch.isupper():
        character.append(ch)
    elif ch.isdigit():
        digits.append(ch)
    else:
        symbol.append(ch)
print(character)
print(digits)
print(symbol)
count_alpha = str(len(character))
count_digit = str(len(digits))
count_symbol = str(len(symbol))
print("The total number of alphabets in str1 is : " + count_alpha)
print("The total count of Numeric values in str1 is: "+count_digit)
print("The total number of symbol in str1 is: " + count_symbol)

# Create a mixed string
# Expected Output: "AzbycX"
s1 = "Abc"
s2 = "Xyz"
s3 = ""
len_s3 = int(len(s1) if len(s1) > len(s2) else len(s2))
print(s3)
print(s2)
print(len_s3)
s2 = s2[::-1]
for i in range(len_s3):
    if i < len(s1):
        s3 = s3 + s1[i]
    if i < len(s2):
        s3 = s3 + s2[i]
print(s3)

# String Character balance test
# Write a program to check if two strings are balanced.
# String 1 and string2 are balanced if all the characters in the s1 are present in s2. The character's position doesn't matter.
# Expected output: True
# make a function which takes input s1 and s2 then iterate through both

def string_balance(s1, s2):
    message = True
    for i in s1:
        if i in s2:
            continue
        else:
            message = False
    return message


s1 = "Yn"
s2 = "PYnative"
message = string_balance(s1, s2)
print("s1 and s2 ate balanced:", message)

s1 = "ynfhh"
s2 = "PyNative"
message = string_balance(s1, s2)
print("s1 and s2 are balanced: ", message)


