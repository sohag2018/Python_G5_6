# join()---> a method of string  ->
'''Concatenate any number of strings. The string whose method is called is inserted
in between each given string. The result is returned as a new string.

The join() method takes iterable – objects capable of returning its members one at a time.
->iterable – objects: List, Tuple, String, Dictionary and Set'''

# Syntax of join()--->string_name.join(iterable)
#string_name: It is the name of string in which joined elements of iterable will be stored.

#(1):
#string will be stored in between:
#s='-'
#iterable obj:
list=["Sohag","Orfat","Lobid","Tofayel","Manir","Sharif"]
s=''.join(list)
print(s) # Output: Sohag-Orfat-Lobid-Tofayel-Manir-Sharif

#(2)-->joining with empty string
list1 = ['s','o','h','a', 'g']
print("    ".join(list1)) #sohag

