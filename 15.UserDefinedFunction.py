#Why do we use function-->to reuse te code
#Syntax:--->def name(arg1,arg2,...): -->argument as per needed


#function for division
def div(x,y):#this function will returns the result for div of two given numbers
    print(x/y)
#function for modulas
def div(x,y):#this function will returns the result for modulas of two given numbers
    print(x%y)
def message(str):
    print(str)

# we can also use return keyword
def modulus(a,b):
    result=a%b
    return result
def rarea(l,w):
    print("Area:",end="")
    return l*w

#with if else
def largNum(a,b):
    if a>b:
        print("LargerNum:",a)
    else:print("LargerNum:",b)


#Let's use our function

# a=10
# b=20
a=int(input("Enter 1st Num: "))
b=int(input("Enter 2nd Num: "))
add(a,b)  # we ju.st call the function and pass the arg and in return we will find the sum of a and b
sub(a,b)
multi(a,b)
div(a,b)
message("Hellow")
print(modulus(a,b))
print(rarea(a,b))
largNum(a,b)


