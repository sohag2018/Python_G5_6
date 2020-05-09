#Here we will se the use of sub()--->we can find a patern->replace with the new one from the text
#Have a look:
#Syntax:-->re.sub(pattern,replace-str,from-text,count=?
#count=1-->if 1 it will only replace 1st matched (even there are few matches), if 2 then first 2 matches will be replaced
# it returns str obj.

import re
pattern=r"colour"
text="My favorite colour is red"

revisedText=re.sub(pattern,"color",text)
#revisedText=re.sub(pattern,"color",text,count=1)
print(revisedText)

