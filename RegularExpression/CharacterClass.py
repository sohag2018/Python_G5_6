#here character class means->group of character

import re
#character should be in a []
print("_____________matching for aeiou___________________")
pattern=r"[aeiou]" #means any of the listed char at the being
if re.match(pattern,"capple"):#could be apple, ijdljfs, udflj whatever starting with listed char
    print("Matched")
else:print("Unmatched")

print("_____________matching for A-Z___________________")
pattern1=r"[A-Z]" #means any of the character should be matched at the begining
if re.match(pattern1,"AapplE"): #cant be applE, but could be Zapple, Bajdljdl
    print("Matched")
else:print("Unmatched")

print("_____________matching for 1-9___________________")
pattern2=r"[1-9]" #means any of the numericcal character should be matched at the begining
if re.match(pattern2,"1applE"): #can be 9applE, but could not be apple9, aj8dljdl
    print("Matched")
else:print("Unmatched")


print("_____________matching for more char class___________________")
pattern3=r"[A-Z][a-z][0-9]$" #means first any char from A-Z then any char from a-z then any num 0-9
if re.match(pattern3,"Aa1"):#could be Aa1ffd, Bb0dkjl only first 3 char seq should be ok
    print("Matched")
else:print("Unmatched")
#Note: if we use r"[A-Z][a-z][0-9]$"-->$ at the end means locked no more then sequential char

