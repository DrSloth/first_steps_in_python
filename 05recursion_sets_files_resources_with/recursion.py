# Recursion means that a functions definition contains itself.
# We call a function recursive if it calls itselfs

# Recursion can be used to implement many mathematical functions for instance 
# the factorial which is inherently defined recursively.
# The two main mathematical definitions look like this

# n! = n * (n - 1) * (n - 2) ... * 3 * 2 * 1
# or
# 0! = 1
# 1! = 1
# n! = n * (n-1)!

# Function to calculate the factorial of n
def factorial(n):
    # The so called base case at which we break the recursion 
    if n <= 0:
        return 1
    else:
        # The recursion step where we recurse one step deeper
        return n * factorial(n-1)

print(factorial(4)) # prints 4!
print(factorial(5)) # prints 5!

# Generally using recursion is not recommended and iteration should be preferred.
# For one recursion is easy to mess up badly which might have consequences in 
# lower level languages (python just raises an exception if we recurse too much)
# Also recursion has to store more data than we actually need to store.
# However it is really common in pure functional languages like Haskell.

# iteratively calculate the factorial of n
def factorial_iter(n):
    fact = 1
    for i in range(1, n):
        fact *= i
    return fact * n

print(factorial_iter(4))
print(factorial_iter(5))
