file=open("student.txt","r+")  #mode-->r=read, w=write r+=read/write
#check readable/writeable
print("--->File is readable/writeable:")
print(file.readable()) #if mode is "w" returns false and "r" returns true, r+ returns true
print(file.writable())#if mode is "w" returns ture and "r" returns false, r+ returns true

##read file-->read()
#print("---> read by using read():")
# text=file.read()
# print(text)
#print(len(text)) #find the size of the file-->How many char

## read each line and put in a list->Need to comment out read() method first
print("--->read by using readLines():")
listText=file.readlines()
print(listText)
print(listText[0]) # print first line

print("--->print by using for lop->readLines():")
for i in listText:
    print(i)


#close file:
file.close()