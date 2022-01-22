# Modules can be used to make code easy to reuse, export and share.
# Modules are imported using the import keyword

# Directly import a module (this is the preffered method)
import random
print(random.randint(1, 6)) # prints a randomly generated number between one and six

# You can also import a single item from a module with the
# `from module import item` syntax
from math import pi
print(pi) # Prints a relatively usable value of py

# You can also rename imported items with as
from math import sqrt as square_root
print(square_root(4)) # Prints the square root of 4

# With an asterisk (*) all items can be imported
from random import *
print(randint(1, 6)) # Same as above

# These modules are all part of the standard library also called std
# which means they are always available when using python.
# Documentation of the standard library can be found at 
# https://www.python.org
