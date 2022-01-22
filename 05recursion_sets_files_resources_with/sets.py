# Sets are another important data structure.
# Sets are only meant to store the information that something exists/is in the set.
# This also means data is unique inside the set

nums = {1, 2, 3, 4, 1, 2, 3}

# We can iterate sets
for i in nums:
    print(i)

# We can check wether a value exists in a set with the in keyword
if 3 in nums:
    # The in keyword actually also works for lists but its faster with sets
    print("Three is part of nums")

# The in keyword can be negated with not
if 5 not in nums:
    print("Five is not inside nums")
