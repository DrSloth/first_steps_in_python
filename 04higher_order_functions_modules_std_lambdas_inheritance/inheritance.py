# Inheritance can be used to show relations between classes with inheritance
# you generally always speak from one class specializing the other class

# For instance a Pet class defined by its name and pat method
class Pet:
    def __init__(self, name):
        self.name = name

    def pat(self):
        print("You just pat " + self.name)

# You can use the class childclass(superclass) syntax to inherit from a class
# This means a 'childclass' is a special version of a 'superclass'
class Cat(Pet):
    # Cats can meow
    def meow(self):
        print("meow")

# All Dogs are Pets, but not all Pets are dogs.
# Dogs can also bark but not all Pets can.
class Dog(Pet):
    def bark(self):
        print("WOOF!")

doge = Dog('Doge')
doge.bark()
doge.pat()
# you cant do doge.meow()
kitty = Cat('KitKat')
kitty.pat()
kitty.meow()
