# Higher order functions are functions that take other functions as parameter 

# This function prints its parameter two times
def print2times(x):
    print(x)
    print(x)

def print3times(x):
    print(x)
    print(x)
    print(x)

# This function calls the function it takes as parameter on each digit
def for_digits(f):
    for i in range(0, 10):
        f(i)

# The function can be passed as parameter like other variables
for_digits(print3times)
