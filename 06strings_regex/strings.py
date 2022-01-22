# Strings are used for storing text, they are important as any kind of terminal input and output
# completely rely on them. Being able to use and understand them is vital.  

# This is a simple string
hello = "Hello, World!"

# Prints Hello, World! to the terminal
print(hello)
# Prints the len of "Hello, World!" which is 13
print("Len of hello: " + str(len(hello)))

# On a very fundamental level strings store, just as pretty much anything else, just bytes.
# How they are interpreted depends on the programming language you are using and the so called
# string encoding. An encoding defines how these bytes are interpreted 

# Store the bytes of hello in hello_bytes
hello_bytes = bytes(hello, 'utf-8')

# Print the bytes to the terminal
print("Bytes of hello: " + str(hello_bytes))
# Print the lenght of the bytes to the terminal
print("Len of bytes of hello:", len(hello_bytes))

# This is an emoji stored as string
flushed_face = "😳"

# Prints the emoji to the terminal
print(flushed_face)
# This prints the len of the string containing the emoji to the terminal.
print(len(flushed_face))

flushed_face_bytes = bytes(flushed_face, 'utf-8')

# Print the bytes of the emoji to the terminal
print("Bytes of 😳:", flushed_face_bytes)
# Print the lenght of the bytes to the terminal
print("Len of bytes of hello:", len(flushed_face_bytes))
