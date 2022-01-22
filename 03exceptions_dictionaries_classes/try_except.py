# To handle exceptions you can use the try an except keywords

try:
    # Division by zero is not allowed. Even if it is 0 / 0
    0 / 0
except ZeroDivisionError:
    print("Dividing by zero is illegal (you will go to jail)")

# This function will always "fail" and thus raise an error
def always_fails():
    # This exception is unhandled but no error is given directly
    raise Exception("Bad error")

try:
    # The exception is handled here because of the try
    always_fails()
except Exception as e:
    #directly assign the catched exception to e
    print("An error occured: ")
    # print the message of e
    print(e)

# The error here is unhandled and an error is shown
always_fails()
