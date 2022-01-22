# The remove function from the os module can be used to remove files
import os
import sys

# remove the file given as first user argument
os.remove(sys.argv[1])
