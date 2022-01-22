# Dictionaries store key value pairs 

# Dictionaries can be created using the {} syntax
dog = {
    # Keys are always on the left and values on the right they are divided by a colon (:)
    "cute": True,
    "name": "Jack",
    # Keys don't have to be strings, they can be almost anything
    10: "age",
    "breed": "Golden retriever"
}

# To get a value out of a dictionary you can use the index operator ([])
print(dog["cute"])
print(dog["name"])
print(dog[10])
print(dog["breed"])

# Get the length (the number of different keys) in a dictionary
print(len(dog))
