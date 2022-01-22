# If statements can be used to conditionally execute some code
# they accept any expression which evaluates to a boolean

if 10 > 5:
    # Python is indentation sensitive everything that is indented here belongs to the if
    # normally 4 spaces are used as indentation
    # text editors like vscode also support converting tabs automatically to 4 spaces 
    print("Yay Math works") 
    print("hello")

# For clarity:
# The previous if could also have been written as:

a = 10 > 5 # a holds the value True

if a: 
    print("This also works")

# This works because variables are expressions which evaluate to whatever value
# they are currently holding.
