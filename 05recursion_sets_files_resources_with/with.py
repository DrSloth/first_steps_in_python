# Things like files are called resources. They are gicen by the operating system and 
# have to be disposed of after being done with.
# We have to close files for instance

fd = open("with.py", "r")
print(fd.readline())
fd.close()

# In order to do this a bit more automatic you can use with 
with open("with.py", "r") as f:
    # do stuff with f here
    print(f.readline())

# f is closed automatically here
