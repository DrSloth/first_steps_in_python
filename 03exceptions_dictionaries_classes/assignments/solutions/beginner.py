class Greeter:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print("Hello, " + self.name + "!")



# Test:
g = Greeter("Asuka")
g.greet()
g.greet()
