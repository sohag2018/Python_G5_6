##Some Meta Characters are:
#      .(dot)(any character)
#      ^ and $
#      *  means->(0 or more)
#      + means->(1 or more)
#      ? (0 or 1)
#      {and}$

import re
print("_____________using of dot_________________________")
#dont forget->match() will check at the begining
pattern=r"col.r" # we can put more dot
if re.match(pattern,"col r of blood is red"): #whatever we put in between l_r it will be accepted
    print("Matched")
else:print("Unmatched")

print("_____________using of ^ and $________________________")
pattern1=r"^co..r$"
if re.match(pattern1,"coxxr"): #str must ends by r -->if we put "coxxr of blood is red" will not work
    print("Matched")
else:print("Unmatched")


print("________using * (0 or more times) 1_____________________")
pattern2=r"a*"  #means in the pattern 'a' can be 0 or any number of time
if re.match(pattern2,"color"):  # we can put caalor
    print("Matched")
else:print("Unmatched")

print("________using * (0 or more times) 2_____________________")
pattern5=r"a*b"  #a can be 0 or more then b. If no a then b at the begining
if re.match(pattern5,"ablor"): # we could put blor, aablor, aaablor
    print("Matched")
else:print("Unmatched")


print("________using + (1 or more times) 1_____________________")
pattern3=r"a+"  #means in the pattern 'a' can be 1 or more than 1 time
if re.match(pattern3,"alor"):  # a must be at the begining (aalor,  alore , aaaaa, a )
    print("Matched")
else:print("Unmatched")

print("________using + (1 or more times) 2_____________________")
pattern4=r"a+b"  #means in the pattern 'a' at the beging then b
if re.match(pattern4,"ablor"):  # a must be at the begining then b
    print("Matched")
else:print("Unmatched")


print("________using ? (0 or 1 times) _____________________")
pattern6=r"ice(-)?cream"  #means (-) can be 0 or 1 times not more than 1
if re.match(pattern6,"icecream"):  # we could use ice-cream but not ice--cream
    print("Matched")
else:print("Unmatched")
#Note: in pattern we could use r"ice(-)?cream" or r"ice--?cream" or r"ice(--)?cream"
#if we put r"ice(--)?cream" means 0 times -- or 1 time --   ->considers a single entry

print("________using {_,_} (min_ and max_ times) _____________________")
pattern7=r"a{1,3}$"  #a can be min 1 and max 3 times but need to use $ -> no other char is allowed
if re.match(pattern7,"b"):  # we could use ice-cream but not ice--cream
    print("Matched")
else:print("Unmatched")
#Note: in patter if we use r"a{1,3}" then  a can be used 1-any number of times and othe char too
#if we use-> r"a{3}" then a must be 3 times consecutively then other char can be or not
#if we use-> r"a{0}" then a can be 0 or any number of times
