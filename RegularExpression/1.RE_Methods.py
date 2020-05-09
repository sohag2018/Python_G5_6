import re

#taking a pattern
pattern=r"color" #r-->row/raw str? confused need to know, f--? may be formulaiton
print("---------using-match()---------------------------")
#matching by using regex method--match()-->check only at the begining of the string
if re.match(pattern,"Red is a color of blood"):
    print("Matched")# didnt find at the begining
else:
    print("Not Matched")

print("--------------using-fullmatch()-----------------------")
#fullmatch()--> need to match all of the string, returning a Match object, or None
if re.fullmatch(pattern,"color"):
    print("Matched")# full match
else:
    print("Not Matched")

print("-------------using-search()------------------------")

# searching pattern any where in string
if re.search(pattern,"Red is a color of blood"):
    print("Matched")  # found but not at the beging
else:
    print("Not Matched")

print("-------------using-findall()------------------------")
#findall() will search and return a list-->if more than one then return all---otherwise returns []
print(re.findall(pattern,"Red color: It is a color of blood"))

print("--------------using-split()-----------------------")
#split() gets the patern matched and split into pcs up to max(as per highest split size)
print(re.split(pattern,"Red color is a color of blood color",2)) #['Red ', ' is a ', ' of blood']

print("--------------------------------------")
#