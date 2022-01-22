# Python uses the utf-8 encoding by default. utf-8 is a common standard around the world
# and is absurdly flexible, it supports pretty much all languages and emojis you can think of.

# UTF8 works in three orders of character representation.
# 1. Bytes: Just single bytes not very helpful to display emojis
# 2. Scalars: Multiple bytes together to form something like an emoji
# 3. Grapheme Cluster: Might contain multiple scalars put together  

# A hindi letter
hindi_char = "ते"
# Outputs ते to the screen 
print(hindi_char)
# Outputs 2 because ते consists of two scalars 
print("Len of hindi char:", len(hindi_char))
print("hindi char bytes:", bytes(hindi_char, 'utf-8'))

# Output all scalar values on their own
for c in hindi_char:
    print(c)
