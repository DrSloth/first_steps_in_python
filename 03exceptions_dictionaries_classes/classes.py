# Define a class called Dog
class Dog:
    # The __init__ method is called a constructor and is used to create
    # instances of a class (also called objects)
    def __init__(self, name, age):
        # We have the thre fields name, age and cute
        self.name = name
        self.age = age
        self.cute = True

# You can create an object of a class by calling the classname of a class as function 
jack = Dog("Jack", 10)
# access the name field of jack
print(jack.name)
print(jack.cute)

# Create a dictionary filled with values important to modell a cat
def cat(name, age):
    s = {"name": name, "age": age, "cute": True}
    return s

# Create a cat called meow. 
meow = cat("meow", 20)
print(meow["name"])
print(meow["age"])


# Side Note:
# Programming with objects is commonly called Object Oriented Programming or OOP for short.
# The first approach we used with the Dog is called Class based OOP because we use a Class to model
# how we create Objects and define Methods on them and how polymorphism works (more on this later)
# There are a lot of Programming languages which use this concept a lot like:
# Java, C#, C++ and a lot of other languages which support it like Python or newer versions of JavaScript
# The approach we used on the cat is closer to what is called Prototype based OOP
# we have the cat as prototype and can freely "clone" it (as we do in the cat function), then we can 
# easily mutate it by giving it new fields or mutating existing ones.
# Languages that support this directly also have something like a prototype field which
# tells the language "if the requested property is not in this object look in its prototype"
# Language that are based on this approach include:
# Lua, Self and JavaScript (more dominant than Class based because Class based OOP was added later)
