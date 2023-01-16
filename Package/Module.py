# Modules -- A file containing python codes -- which are related to each other
# Import the file name and then the function and call the function as object

from fibo import calc_shipping, calc_tax
# another way of importing is
import fibo
import sys
# Then as a method
fibo.calc_shipping()
fibo.calc_tax()
# As a function
calc_shipping()
calc_tax()
# Compiled Python Files
# Compares the date and time of py-cache and the module and if module has been modified it will recompile it to update the version of py-cache
# Module search Path
# Package is a container -- for one or more module
# Sub-packages
# Intra- package
# the dir function -- for debugging

print(dir(fibo))
print(fibo.__name__)
print(fibo.__package__)
print(fibo.__file__)
print(sys.path)
print(__name__)
# Executing Modules as Scripts
