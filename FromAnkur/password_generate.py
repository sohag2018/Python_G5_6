import string
import random
'''def add(x,y,z=0):
    return x+y+z
print(add(5,6))
print(add(5,6,10))'''

def pw_generate (size=1,chars=string.ascii_letters+string.digits+string.punctuation):
    return ''.join(random.choice(chars) for _ in range (size))


print(pw_generate(int(input('How many characters in your password?'))))