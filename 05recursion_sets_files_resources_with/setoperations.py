# Sets support multiple mathematical operations

first = {1, 3, 4, 5, 6, "hallo"}
second = {4, 5, 6, 7, 8, 9, 200, 42}

first.add(2)
first.remove("hallo")

#The union operator `|` combines all items from both sets.
print(first | second)
# The intersection operator `&` gets items contained in both
print(first & second)
# The difference operator `-` gets items in the first set but not in the second.
print(first - second)
print(second - first)
# The symmetric difference operator ^ gets items in either set, but not both.
print(first ^ second)
