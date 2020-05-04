#range() produce a range of elements
num=list(range(10))#need to store in list-->converted to list--typecast
print(num)  # -->[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]--->these are the values in same number of index
print(num[5])# -->5 in index [5]

#partial range (starting value and ending value--index always starts from 0--->)
num1=list(range(5,11)) #from 5 to 10
print(num1) # -->[5, 6, 7, 8, 9, 10]

#partial range & interval (starting value and ending value--index always starts from 0--->)
num2=list(range(5,21,2)) #from 5 to 20 value
print(num2) # -->[5, 7, 9, 11, 13, 15, 17, 19]
print(num2[0]) #5
print(num2[-1])#19
print(len(num2))#8



