# Regular expressions can be used to easily match patterns inside strings.
# They are very important, espacially in web programming where you have to validate a lot of text.

# In order to use regex we need the 're' module
import re

# The r tells python that this is raw string. Raw strings are useful because they allow you to use
# the \ character as much as you want. In normal strings you would have to use \\
pattern = r"spam"
text = "spamspamspam"

# This does match because text doesn't have any substring which doesn't match the pattern
if re.match(pattern, text):
    print(pattern, "does match", text)
else:
    print(pattern, "does not match", text)
