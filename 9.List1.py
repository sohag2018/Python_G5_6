#List---> an obj of Python where we can store data

subject=["C","C++","Python", "Java","Ruby"] # we can store int,double,str --->subject is the name of list
#subject.append("one") #adding
print(subject) #to print all--print the List
print(subject[0])#to print [0] index value-->C
print(subject[:2])#to print from [2] index & above index -->Python, Java, Ruby
print(subject[2:])#to print from [2] index & above index -->Python, Java, Ruby
print(subject[-1])#to print last index-->Ruby

#to check the position of the item
position=subject.index("Java") #it will return int
print("Java is in:",position)#3

#to check number of occurance
count=subject.count("Java")
print("Occurance of Java:",count)

# to check element is available in list or not-->returns True/False
print("Python" in subject)  #True
print("swift" in subject)  #False
print("swift" not in subject)  #True

# to add more in our list

print(subject+["swift"])#It will be added as concatenate
print(subject)
print("swift" in subject)  # False-->previous line actuly didnt add in actual list-->need to use append() for adding
subject.append("swift")#will be added last
print("swift" in subject)#this time it will show True
subject.insert(2,"Java Script") # will b added in 2 index position and previous items will be shifted to next position
print(subject*2)#It will print  the items twice
print(len(subject)) # it will print the lenght of the list--->7

#to remove
subject.remove("swift")
print(subject," & Length: ",len(subject))


# to sort
list1=[1,8,9,2,8]
list1.sort() # Accesding order  only for int
print(list1)
subject.sort()  #we faced a proble to sor after adding by append()
print(subject)

subject.reverse()#Descending
print(subject)

#To copy and store in new list
subject2=subject.copy()
print("subject2: ",subject2)

subject3=["sfk","lsflj"]
subject2.extend(subject3)
print(subject2)
print(subject3)
#to clear the list items
subject2.clear()
print(subject2) # []---no value
del subject3
#print(subject3) #-->will show not defined












