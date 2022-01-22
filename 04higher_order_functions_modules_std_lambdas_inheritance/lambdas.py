# Lambdas are often used together with higher order functions
# they can be used to create inlined functions which don't have
# to be defined or seperately and named. Many languages call them
# anonymous functions because they have a no strictly assigned name.

# This functions calls its parameter function two times
def do_twice(f):
    f()
    f()

# Lambdas are restricted to a single expression
do_twice(lambda: print("Hello, World!"))

# Many builtin functions take higher order functions.
# For instance the map function which applies an operation to
# each element of a list. 

# Create a list with some numbers
nums = [2, 4, 6]
# Lambdas can take parameters by writing its name before the :
result = list(map(lambda x: x*2, nums))
print(result)
