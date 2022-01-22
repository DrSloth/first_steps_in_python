class Adder:
    def __init__(self, b):
        self.b = b

    # This creates the add_numbers method which has acces to self
    def add_numbers(self, a):
        # self allways is the object this method is called on
        return a + self.b

# Create an adder where self.b = 10
ad = Adder(10)
# In add_numbers the self parameter will be equal to ad
print(ad.add_numbers(20)) # Prints 30
