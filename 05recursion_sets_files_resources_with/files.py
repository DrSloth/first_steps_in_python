# Working with files is very common in programming. 
# Knowing how to work with them is vital in most languages.

# You can open files with the open function.
# The open function accepts a path and a filemode as parameter

# First open a file for writing ("w"), creating it if it doesn't exist.
file = open("hello.txt", "w")

# The file will be empty because "w" truncates existing files
# We can now write to file using the write function
file.write("Hello, World!")
# After being finished with a file we want to close it to release the ressource
file.close()
