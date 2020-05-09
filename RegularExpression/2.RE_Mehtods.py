#In this program we will see different methods associated with search() return obj

import re
pattern=r"color"
text="My favorite color is red"

#search() returns obj:
match=re.search(pattern,text)
if match:
    print(match.start()) #will return starting index of matched obj
    print(match.end()) #will return ending index of matched obj
    print(match.span()) #will return starting-ending index of matched obj