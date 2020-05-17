print("# define variables in a single line:---------")
a,b,c=10,20,30
print("a=",a)#10
print("b=",b)#20
print("c=",c)#30

print("# same value many variables:----------------")
x=y="Hello"
print("x=",x) #Hello
print("y=",y)#Hello

print("# gloabal and local variable----------------")
name1="I am outside of func-->global"
print(name1)
def var():
    name2="I am inside func-->local"
    print(name2)
var()


print("# same name for global & local:-(no change)-------")
age=40
print("global age:",age)
def varAge():
    age=50
    print("local age:",age)
var()

print("# uses of local and global-----------------------")
id1 = 101


def varId():
    id2 = 102
    print("global id call from func", id1)
    print("Local id call from func", id2)


varId()
print("global id call out side of func:", id1)
print("loca id call out side of func:", "sorry first make it global")

print("# make local var-->global in func----------------")
def varCity():
   global city
   city="woodside"
   print("Call from func",city)

varCity() #call must
print("call as gloabl:",city)


print("# make global var-->local in func")

phone=3474005813
def varPhone():
    global phone
    phone=1464646464

varPhone() #call must
print(phone)




