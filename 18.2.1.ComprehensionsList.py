##Befor Comprehension List
num=[1,2,3,4,5]  #list
#squre all the values-->map funciton with lambda expression:
result=list(map(lambda x:x*x,num))
print(result) #output-[1, 4, 9, 16, 25]
print("_______________Comprensions lit_________________________")
##Now let's see how Comprehension list works
# Syntax-->do everythin in []  use a for each loop-->put value in a variable   now manupulate new variable as per your need
#[x for x in num]
result=[x*x for x in num] #-->put the num-value in x (for each loop)-->each x value is multiplyng by itself (first x)
print(result)

print("____________filter function with Comprehension list______")
## now let's see for filter function with Comprehension list

# first what we did before filter funciton with lambda function
#function to find the even number
result=list(filter(lambda x:x%2==0,num))
print(result)
print("_______________Comprensions lit_________________________")
#Let's try with Comprensions lit
result=[x for x in num if x%2==0] #--> put the num-value in x variable (for each loop )-->each x value is checking in condition it true then print
print(result)


