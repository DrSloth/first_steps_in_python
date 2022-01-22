# Normal programs used from the command line take input in the form of arguments
# In order to get the arguments in python we need the sys module
import sys

# This prints all arguments
print(sys.argv)

# This prints the first argument which is the file executed by the python interpreter
print(sys.argv[0])

# Prints the first argument given by the user if it exists 
if len(sys.argv) > 1:
    # The args are always strings
    print("Your first arg is: " + sys.argv[1])
