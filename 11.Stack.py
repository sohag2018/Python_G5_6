#Stack-->Data Structure
#pop--->remove the data
#Stack follows LIFO--->so pop removes last entered data

books=[]  #empty list
books.append("Sohag")
books.append("Sharif")
books.append("Orfat")
books.insert(0,"Monir")  #it will not be removed by pop


for i in books:
    print(i)

print("---------------------")
books.pop()
for i in books:
    print(i) #it will not print Orfat--->removed by pop()-->LIFO , Monir's index is 0 not the last index

print("---------------------")
#Let's see now who is at the top position (last index-->[-1])
print(books[-1]) #Sharif

print("---------------------")
#let's pop again-->remove Sharif
books.pop()
for i in books:
    print(i)# Sharif is not here, removed by pop as it wast the top

print("---------------------")
#What happen if there is no value at all
books.pop()
books.pop()
if not books:    # if not...object  represent Do.....when it is empty
    print("No books left")




