# One important iterable is the range object created with the range function
# The range creates values from the first parameter (inclusive) until 3 (exclusive)
r = range(0,3)
iterable = iter(r)

print(next(iterable)) # prints 0
print(next(iterable)) # prints 1
print(next(iterable)) # prints 2
