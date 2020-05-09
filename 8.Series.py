#create a series like 1+2+3.......+n

n=int(input("Enter the last number: "))
sum=0
for i in range(1,n+1,1):
        sum=sum+i
        print(i, end="")
print("\nSum:",sum)

#create a series like 2+4+6.......+n
n2=int(input("Enter the last number: "))
sum2=0
for x in range(2,n2+1,2):
        sum2=sum2+i
        print(x,end="")
print("\nSum:",sum2)

#create a series like 1+3+5.......+n
n3=int(input("Enter the last number: "))  #if 10-->1+3+5+7+9=25
sum3=0
for y in range(1,n3+1,2):
     sum3=sum3+y
     print(y, end="")
print(sum3)

#create a series like 1^2+2^2+3^+……........+n, when n=5--> 1+4+9+16+25=55
n4=int(input("Enter your last number: "))
sum=0
for a in range(1,n4+1,1):
    sum=sum+a*a
    print(a, end="")
print("\nSum:",sum)

# create a series like 1*2*3......*n  when n=5-->1*2*3*4*5=120
n=int(input("Enter your last number: "))
result=1
for i in range(1,n+1,1):
    result=result*i
print("\nResult:",result)
