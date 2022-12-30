
# use breakpoint()
import sys
x = 5
y = 6
z = x + y
print(z)
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
# A class in an except clause is compatible with an exception if it is the same class or base class
class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    # except B:
    #     print("B")
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
# if the except clauses were reversed i.e except B first it would have printed B,B,B
# The except clause may specify a variale agter the exception name.
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))    # the exception instance
    print(inst.args)     # arguments stored in .args
    print(inst)          # __str__ allows args to be printed directly,
                         # but may be overridden in exception subclasses
    x, y = inst.args     # unpack args
    print('x =', x)
    print('y =', y)

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:", err)
except ValueError:
    print("Could not convert data to an integer.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise

for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
def this_fails():
    # x = 0/1
    x = 1/0

# try:
#     this_fails()
# except ZeroDivisionError as err:
#     print('Handling run-time error:', err)
#
# try:
#     raise NameError('HiThere')
# except NameError:
#     print('An exception flew by!')
#     raise

# Exception Chaining
# try:
#     open("database.sqlite")
# except OSError:
#     raise RuntimeError("unable to handle error")

# def func():
#     raise ConnectionError
#
# try:
#     func()
# except ConnectionError as exc:
#     raise RuntimeError('Failed to open database') from exc

try:
    # raise KeyboardInterrupt
    pass
finally:
    print('Goodbye, world!')
# Finally clause will be executed as the last task before the try statement completes
def bool_return():
    try:
        return True
    finally:
        return False
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    except TypeError:
        print("Type Error")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

divide(2, 1)


divide(2, 0)


divide("2", "1")
# Pre defined clean up actions
# def f():
#     excs = [OSError('error 1'), SystemError('error 2')]
#     raise ExceptionGroup('there were problems', excs)
#
# f()
#
# try:
#     f()
# except Exception as e:
#     print(f'caught {type(e)}: e')

excs = []
def f():
    raise ExceptionGroup("group1",
                         [OSError(1),
                          SystemError(2),
                          ExceptionGroup("group2",
                                         [OSError(3), RecursionError(4)])])

try:
    f()
except OSError as e:
    print("There were OSErrors")
except SystemError as e:
    print("There were SystemErrors")

