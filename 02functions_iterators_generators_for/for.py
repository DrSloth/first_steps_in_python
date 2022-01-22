# For loops are used ot iterate over all elements of an iterable
# They use use the 'for variable in iterable' syntax

for i in range(0, 3):
    # x is defined in the for loop and usable in this body of the for loop
    print(i) # prints 0, 1, 2 each on a new line

for i in [10, "Hello", "World"]:
    # We call this iterating through an iterable
    # Here it would be called iterating through a list
    print(i) # prints 10 then Hello and then World each on a new line
