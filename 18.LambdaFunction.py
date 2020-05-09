#Lambda Function--->is a function which has no name (without name)
#not powerful comparing with named function
#generaly it works with single expression/single line

#named function-->to find the value of (a+b)^2-->a^2+2ab+b^2
def calculaiton(a,b):
    return a*a+2*a*b+b*b
#Call the function
print(calculaiton(2,3)) #4+12+9=25
print("----------------seperator--------------------------------")
#Lambda syntax:--> (lambda parameters: expression)(value of param)
print((lambda a,b:a*a+2*a*b+b*b)(2,3))  #25

# OR
# a=(lambda a,b:a*a+2*a*b+b*b)(2,3)
# print(a)  #25
print("----------------seperator--------------------------------")

#named function-->to find the value of a^3-->a*a*a
def calculaiton(a):
    return a*a*a
#Call the function
print(calculaiton(3)) #27
print("----------------seperator--------------------------------")
#Lambda syntax:--> (lambda parameter: expression)(value of param)
print((lambda a:a*a*a)(3))  #25
print("----------------seperator--------------------------------")


