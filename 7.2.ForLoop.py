num=[10,20,30,40,50,60]
print(num)#output-->[10, 20, 30, 40, 50, 60]
print(num[0])#output-->10

#using while loop to traverse
index=0
length=len(num)
while index<length:
    print(num[index],end=" ")
    index=index+1
print("")

#For loop
for i in num:    #after traversing value will be stored in i--->so we need to print i
    print(i,end=" ")
print("")# just for a new line before new print statement

# sum by using for loop
sum=0
for i in num:
    sum=sum+i
print(sum)



