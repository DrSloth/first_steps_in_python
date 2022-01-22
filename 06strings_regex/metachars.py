# A metacharacter does have another meaning then is literal character

import re

text = "spam eggs"

# A dot can be used to match any character, an asterisk to repeat the previous char
if re.match("\.", text):
    print(text, "contains characters")

if re.match(".+", "hudfhuh23121!!"):
    print("Matches")

if re.match(".*", ""):
    print("Matches2")

if re.match(".+", ""):
    print("Matches3")

if re.match("^spam.*", text):
    print(text, "starts with spam")
