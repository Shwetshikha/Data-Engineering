# Get input from user to store name phone and email for 3 users
# open txt file and write to it these values in the form of dict
# get these values from txt file
import json
data = {}
# for i in range(1):
#     name = input("Enter your name")
#     phone = input("Enter your phone")
#     email = input("enter your email")
#     data[name] = name, phone, email
# print(data)
# with open("data.txt",'w') as file:
#     # file.write(json.dumps(data))
#     for key,value in data.items():
#         file.write('%s:%s\n' % (key,value))


class details:

    def input_details(self):
        n = int(input("The number of details you want to enter"))
        for i in range(n):
            name = input("Enter your name")
            phone = input("Enter your phone")
            email = input("enter your email")
            data[name] = name, phone, email
        print(data)
    def convert_json(self, dict):
        with open("data.txt", 'w') as file:
            # file.write(json.dumps(data))
            for key, value in data.items():
                file.write('%s:%s\n' % (key, value))
    def read_json(self):
        file1 = open("data.txt", 'r')
        line = file1.readlines()
        count = 0
        for line in line:
            count += 1
            print("Line{}: {}".format(count, line.strip()))


    def get_detail(self):
        user = input("Enter the name of user for which you want to show info")
        detail = dict([key, value] for key,value in data.items() if key == user)
        print(detail)



entries = details()
entries.input_details()
entries.convert_json(data)
entries.read_json()
entries.get_detail()