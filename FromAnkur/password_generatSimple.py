import random
import string
#getting input from user for lenght of the password
len=int(input(print("How long you want your password? ")))
#getting string for str separator (no space->'')

#concatenate and  storing string of ASCII char
strMix = string.ascii_letters + string.punctuation + string.digits

#using join() to join randomly generated char and concatenate and restoring in str1 var:
str1= "".join(random.choice(strMix)
                for _ in range(len)) # traversing on iterable obj
print(str1)







