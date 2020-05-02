#List---> an obj of Python where we can store data

subject=["C","C++","Python", "Java","Ruby"] # we can store int,double,str --->subject is the name of list
print(subject) #to print all--print the List
print(subject[0])#to print [0] index value-->C
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

print(subject+["swift"])
print("swift" in subject)  #True but still it will show False-->previous line actuly didnt add in actual list-->need to use append() for adding
subject.append("swift")#will be added last
print("swift" in subject)#this time it will show True
subject.insert(2,"Java Script") # will b added in 2 index position and previous items will be shifted to next position
print(subject*2)#It will print  the items twice
print(len(subject)) # it will print the lenght of the list--->7

#to remove
subject.remove("swift")
print(subject," & Length: ",len(subject))

# to sort
subject.sort() # Accesding order
print(subject)

subject.reverse()#Descending
print(subject)

#To copy and store in new list
subject2=subject.copy()
print("subject2: ",subject2)

#to clear the list items
subject2.clear()
print(subject2) # []---no value










