# With inheritance you can create custom exceptions
# Inheriting from the Exception class makes a thing raisable

# By doing this you create a raisable exception
class BadException(Exception):
    # pass tells python that even though it expects something 
    # there will be nothing following here. 
    # This is used to create empy classes or blocks in general
    pass

try:
    raise BadException
except BadException:
    print("A really bad exception happened")
except Exception:
    print("Another exception")

# You can also add a custom message
class CustomMessageException(Exception):
    def __init__(self):
        # Access the super class with the super() function
        # here we call its __init__ function to give it a message
        super().__init__("This is a custom message")

raise CustomMessageException
