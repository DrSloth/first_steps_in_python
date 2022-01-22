# Similarly to writing files (see files.py) we can open files for reading.

fd = open("files.py", "r")
# we can read all the content of the file at once using the read function
s = fd.read() 
# s contains a string which contains the complete file
print("files.py contains " + str(len(s)) + " characters")
# Files store where they are located (where they are read to) this location is
# called the file pointer with the seek function we can move the files pointer
# seek(0) means to go back to the start of the file and thus reset the file pointer
fd.seek(0)

# we can read only one line with the readline function
print("The first line of files.py is: " + fd.readline())
print("The second line of files.py is: " + fd.readline())

# Reset the file pointer
fd.seek(0)

# we can also iterate all lines
for line in fd.readlines():
    # we can specify the end parameter to tell python what to piut at the end
    # of a print. By default this is the new line character (\n) here we want nothing
    print(line, end="")

