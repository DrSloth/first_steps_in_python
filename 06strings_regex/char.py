#

import re

pattern = "[a-d]"

if re.match(pattern, "a"):
    print("Match1")

if re.match(pattern, "z"):
    print("Match2")

if re.match(pattern, "A"):
    print("Match3")

pattern = "[a-dA-DyY]"

if re.match(pattern, "A"):
    print("Match4")

if re.match(pattern, "y"):
    print("Match5")

pattern = "[0-9]"
# Matches all digits
pattern = r"\d"
# Matches all whitespace
pattern = r"\s"
pattern = r"\w"
pattern = "[a-zA-Z0-9_]"
