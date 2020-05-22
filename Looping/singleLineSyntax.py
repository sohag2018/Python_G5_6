#Double looping at same traversing action
##Need to do:Consecutive pair-->['ab', 'cd', 'ef']

listS=["sohag","Orfat","Lobid","Tofayel","Manir","Sharif"]
#traverse from 0 index and every 2nd indext store in a new list and print it
#Intend to traverse and store in a new list while staying inside the list
listR=[x for x in listS[0::2]]   #List comprehension
print(listR) #Output:['sohag', 'Lobid', 'Manir']
#Explanation: listR=[x for x in listS[0::2]]-->inside the list: 1st x is iteration result
# then as it is looping syntax. Everything is in []  because it is same time stong in a list
# finally list assigned to list var listR.
print("# we could do following way too----------")
listX=[]
for x in listS[::2]:
    listX.append(x)
print(listX) #Output:['sohag', 'Lobid', 'Manir']

##2
for i in listS:
    print(i)
print("# we could following way too----------")
# we could following way too
print(a for a in listS)



##This code should be in join module not related to looping
strS="Sohag"
strS='-'.join(strS)
print(strS)






list1 = ['a', 'b', 'c', 'd', 'e', 'f']
#(1) This is to understand the 2nd one (i did it extra to see how it works)
list2=[]
for i in list1[0::2]: #starts from 0 and every 2nd index
    list2.append(i)
print(list2) #Output: ['a', 'c', 'e']

list3=[]
for i in list1[1::2]: #starts from 1 and every 2nd index
    list3.append(i)
print(list3) # Output: ['b', 'd', 'f']

print(list(zip(list2,list3)))

#(2)
result = [i + j for i, j in zip(list1[::2], list1[1::2])]
print(result)