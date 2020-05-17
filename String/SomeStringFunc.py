'''
Some String Methods:
*** capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning
'''

print("# capitalize(), upper(), lower(), swapcase(), title(), casefold(),isupper(), islower(), istitle()-------")

txt = "hello, and welcome you all."
# txt = "Hello, And Welcome You All."
print("capitalize():", txt.capitalize())  # Hello, and welcome you all.
print("upper():", txt.upper())  # HELLO, AND WELCOME YOU ALL.
print("lower():", txt.lower())  # hello, and welcome you all.
print("swapcase():", txt.swapcase())  # HELLO, AND WELCOME YOU ALL.
print("title():", txt.title())  # Hello, And Welcome You All.
print("casefold():", txt.casefold())  # hello, and welcome you all.
print("isupper():", txt.isupper())  # F
print("isupper():", txt.islower())  # T
print("isupper():", txt.istitle())  # F

print("#center():------------------------------")
txt = "banana"
print(txt.center(20))

print("#count():------occurance------------------------")
txt = "My name is Sohag. This name is very common in Bangladesh."
print(txt.count("name"))

print("#:endswith()-------------------------------------")
txt = "My name is Sohag."
print(txt.endswith("Sohag."))  # endswith(".") etc

print("#:expandtabs()-------------------------------------")
txt = "H\te\tl\tl\to"
x = txt.expandtabs(5)
print(x)

print("#:find()---for the position-----------------------------")
# finds the first occurrence of the specified value.
# almost the same as the index()--But index() method raises an exception and find() returns -1 if not found
txt = "My name is Sohag"
x = txt.find("So")
print(x)

print("#:index()----for the position---------------------------------")
txt = "My name is Sohag"
x = txt.index("So")
print(x)

print("#:format()-----with fraction (f)--------------------")
txt = "Total cost is {p:.2f} dollars!"  # 2f-->.00
print(txt.format(p=49))

print("#:isdecimal()---like isalnum(), isalpha(), isnumeric()----------")
# True if all the characters are decimals (0-9).
# method is used on unicode objects.  (we can use the unicode chart)
txt = "9"
# txt = "\u0033" #unicode for 3
x = txt.isdecimal()
print(x)

print("#:-------------------------------------")
myTuple = ("Sohag", "Orfat", "Sharif")
x = "-".join(myTuple)
print(x)

print("#:ljust()-------------------------------------")
# Returns a left justified version of the string
txt = "S"
x = txt.ljust(5, "#")
print(x, "is a learner.")
# Return a 5 characters long, left justified version of the word "Sohag" -->between first char "S" and next str "i"
# by default it will take space but we can use another arg instead of space-->x = txt.ljust(5,"#")-->S#### is a learner.
# ***   rjust()  ->think opposit right justified


print("#:lstrip(), rstrip() & strip()---for Removing spaces-----")
# lstrip()-->Returns a left trim version of the string-->Remove spaces to the left of the string
# rstrip()-->Returns a right trim version of the string-->Remove spaces to the right of the string
txt = "     Lobid     "
x = txt.lstrip()  # -->Remove spaces to the left of the string
print("Among all", x, "is the best ")

y = txt.rstrip()  # -->Remove spaces to the right of the string
print("Among all", y, "is the best ")

xy = txt.strip()  # -->Remove spaces from left & right of the string
print("Among all", xy, "is the best ")

print("#:partition()---(first occurrence)------------------------------")
# searches for a specified string, and splits the string into a tuple containing three elements.
# 1 - before the "match"
# 2 - the "match"
# 3 - after the "match"

txt = "His name is Sharif. Mr. Sharif is a gentale man."
x = txt.partition("Sharif")
print(x)

print("#:rpartition()---(last occurrence)------------------------------")
y = txt.rpartition("Sharif")
print(y)

print("#:split(), rsplit()-----------------------------------")
txt = "apple, banana, cherry"
x = txt.split(", ")
print("split():", x)
y = txt.rsplit(", ")
print("rsplit():", y)

print("#:zfill()-------------------------------------")
#Fill the string with zeros until it is 10 characters long
txt = "50"
x = txt.zfill(10)
print(x) #0000000050

print("#:splitlines()-------------------------------------")
#Split a string into a list where each line is a list item:
#The splitting is done at line breaks.

txt = "Thank you all\nLet's start our sesson."
x = txt.splitlines()
print(x)

a="Sohag"[0]
print(a)

print("#:-------------------------------------")
print("#:-------------------------------------")
