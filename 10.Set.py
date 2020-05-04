#Set-->data structure
# -->an unordered collection of items->So we can't access value by index number
# No duplicate item/value

#Creation of Set--1) by using curly brace 2) set function
num={1,2,3,4,5,5}  # we put duplicate but it will be counted
num2=set([4,5,6,7,8]) #put values in list then convert into set using set() function

#Adding & Removing value
num.add(6)
num.remove(5) #remove all 5

#Print:
#print(num[0]) #not possible by using index
print(num) # {1, 2, 3, 4, 5}  -->no duplicate value
print(num2)

print(5 in num) # False
print(6 in num) # True


# Other Operations Union
# Union:--> symbol:(|)---->common+uncommon
print(num | num2) # output->{1, 2, 3, 4, 5, 6, 7, 8}
#intersection->symbol: (&) -->only common
print(num & num2) # output ->{4,6}
# difference --> symbol (-)---->remove common values from 1st set and print only rest
print(num-num2)#removes 4,6 -->output {1,2,3}







