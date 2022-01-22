# Logical operators are used to connect multiple booleans together
# The most commonly used logical operators are "and" and "or"
# For instance the question is "10 greater than 5 and 2 less than 10" would be:

a = 10 > 5 and 2 < 10
print(a) # Prints True because a holds the value True

# || could be a question like "is 7/2 less than 5 or 6*3 less than 6"
b = 7/2 < 5 or 6*3 < 6
print(b) # Prints true because 7/2 is less than 5 only one side has to be True

# They can also be mixed
c = a or 5 > 10 and 5 == 4
print(c) # Prints True

# and has higher precedence over or but you can use parenthesis
d = (a or 5 > 10) and 5 == 4
print(d) # Prints False
