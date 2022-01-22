# A regex search can be used to check if the pattern exists in the string

import re

pattern = "spam"
text = "eggs spam sausage spam"

if re.match(pattern, text):
    print(pattern, "does match", text)
else:
    print(pattern, "does not match", text)

if re.search(pattern, text):
    print(pattern, "is in", text)
else:
    print(pattern, "is not in", text)

print(re.findall(pattern, text))
