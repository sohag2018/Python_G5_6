#Map&Filter function works with iterable obj specially with list

#function-->to squre the list value
def square (x):
    return x*x

#list
num=[1,2,3,4,5]

#map function:# it accepts 2 param->1.func and 2.iter1-->so need a func and a iter1/list
result=list(map(square,num))
print(result) #[1, 4, 9, 16, 25]
print("_______________________seperator________________________")

#filter fuction also works with iterable obj-->so we can take a list for that
#what does it do?-->it filters-->it can filter iterable obj-->based on condition it can filter in a list
#if condition fails it removes the element from the list

#let's try with lambda funciton first-->keep only those value which can be dived by 2
num1=[5,10,20,25] #-->list
result1=list(filter(lambda x:x%2==0,num1)) #if condition matched then take it
print(result1) #[10, 20]
print("_______________________seperator________________________")
# named function
num2=["Sharif","Monir","Sohag","Tofayel","Lobid"]

#funciton-->if name starts with 's'

def name(x):
    for i in x:
        if i[0]=='S':
            return i

result2=list(filter(name,num2))
print(result2)


