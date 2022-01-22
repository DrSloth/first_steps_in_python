# A function may take one or multiple parameters 

# x and y are parameters
def f(x, y):
    return x * y + x

# f is called with the two arguments 10 and 20. The order is important!
# Because x is the first parameter and 10 is the first argument every
# x will be replaced with 10 in the function.
z = f(10, 3)
print(z) # prints 40 because 10 * 3 + 10 is 40
