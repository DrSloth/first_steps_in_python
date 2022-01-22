# As briefly mentioned in reading_files.py we can use seek to move the current
# position we are at in the file. This position is called the file pointer.

# seek accepts two arguments the first called offset the second one whence
# whence specifies from where to seek in the file.
# By default whence is 0 which means to seek from the start of the file

fd = open("file_seek.py", "r")

# Move file pointer to the second character from the start of the file
fd.seek(2)
# same as fd.seek(2, 0)

# A whence of 1 means from the current position
fd.seek(3, 1)
# fd is now at the fifth character

# A whence of 2 means to seek from the end of the file
# this moves the file pointer to the end of the file
fd.seek(0,2)
