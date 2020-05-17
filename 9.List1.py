#List---> an obj of Python where we can store data
print("\n## creating list and retrive value of index:-------")
subject=["C","C++","Python", "zayan","Java","Ruby", "Java"] # we can store int,double,str --->subject is the name of list
#subject.append("one") #adding
print("entire list:",subject) #to print all--print the List
subject.reverse()
print("descening",subject)

print("## to get descening first sort then reverse")
list4=[1,5,8,6,7]
print(list4)
list4.sort() #1,5,6,7,8
print(list4)
list4.reverse() #8,7,6,5,1
print(list4)

print("[0] index value:",subject[0])#to print [0] index value-->C
print("[:2] indexe value:",subject[:2])#before 2 all index (upper bound value exclude policy applies)
print("[1:4] indexe value:",subject[1:4])#before 4 all index (upper bound value exclude policy applies)
print("[2:] index value:",subject[2:])#to print from [2] index & above index -->Python, Java, Ruby
print("last index value:",subject[-1])#to print last index-->Ruby
print("\n## check the position of the item:-------")
position=subject.index("Java") #it will return int
print("Java is in:",position)#3 first one will be picked

print("\n## check number of occurance:-------")
count=subject.count("Java")
print("Occurance of Java:",count)

print("\n## check element is available:-------")
print("Python is available:","Python" in subject)  #True
print("swift is available:","swift" in subject)  #False
print("swift is not available:","swift" not in subject)  #True

print("\n## add more in the list:-------")
print("subjec before concatenate:",subject)
print(subject+["swift"])#It will be added as concatenate only list can be concatenated
print("after concatinaiton:",subject)
print("after con swift is enlisted:","swift" in subject)  # False-->previous line actuly didnt add in actual list-->need to use append() for adding
subject.append("swift")#will be added last
print("swift is in list:","swift" in subject)#this time it will show True
subject.insert(2,"Java Script") # will b added in 2 index position and previous items will be shifted to next position
print("list after adding by insert():",subject)

print("\n## muliplying elements in the list-------")
print("check list length:",len(subject))
print(subject*2)#It will print  the items twice
print("Still list length is same",len(subject)) # it will print the lenght of the list--->7


print("\n## to remove----remove()-----------------------")
subject.remove("swift")
print("list after removing:",subject," & Length: ",len(subject))



print("\n## to sort----sort()-------------------")
list1=[1,8,9,2,8]
print("list1 elements:")
list1.sort() # Accesding order  only for int
print("After sorting:",list1)

print("\n## String type lost sorting----------------")
print("Before Sorting:",subject)
subject.sort()  #we faced a proble to sort after adding by append()
print("After Sorting:",subject)
subject.reverse()#Descending
print("After decending Order Sorting:",subject)

print("\n##To copy and store in new list----------------")
subject2=subject.copy()
print("subject2 copy of subject: ",subject2)

print("\n##To extend with existing list----------------")
subject3=["CSS","HTML"]
print("Subject3 list:",subject3)
print("Subject2 list:",subject2)
subject2.extend(subject3)
print("subject2 after extening with subject3",subject2)

print("\n##To clear the list----------------")
print("subject2 before clear:",subject2)
subject2.clear()
print("subject2 after clear:",subject2) # []---no value

print("\n##To del the list----------------")
print("subject3 before del:",subject3)
del subject3
#*** as list will be deleted-->it will show error because no moere subject3
print("subject3 after del",subject3) #-->will show not defined












