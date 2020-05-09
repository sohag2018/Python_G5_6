# single arguments-function
def student(id):
    print(id)

# function call:
student(101)
print("--------------seperation---------------")
# 2 arguments-function
def student(id,name):
    print(id,name)

# function call:
student(101,"Sohag")
print("--------------seperation---------------")

# multiple arguments-function ********nice---->I was looking for it
def student(*details):#argument name anythin is fine
    print(details)

# function call:
student(101,"Sharif")
student(102,"Sohag","Woodside",3474005813)
print("--------------seperation---------------")

# multiple arguments-function ********nice
def add (*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    print(sum)

#function call:
add(5,2)
add(5,2,7,5)
print("--------------seperation---------------")

# XXarguments-function:--->key value pair (like dictionary in python)
def students(**details): #we need to use two-*
    print(details)

#function call:
student1=students(id=101,name="Sharif")
student2=students(id=102,name="Sohag",city="Woodside")
print("--------------seperation---------------")

