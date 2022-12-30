def div(a,b):
    print(a/b)

def smart_div(func):   #

    def inner(a,b):
        if a < b:
            a,b = b,a
        return func(a,b)
    return inner

div1 = smart_div(div)
div1(2,4)
div1(4,12)
div1(16,4)
def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    second_child()
    first_child()
    second_child()

parent()

def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child
    else:
        return second_child
num = 5
parent(num)