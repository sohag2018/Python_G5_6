######Please Comment out to execute following code
# try:
#     list1 = [20, 0, 10]
#     result1 = list1[0] / list1[3]  # there is no [3]->IndexError: list index out of range
#     print(result1)
#     print("Execution Successful") # It will be printed if there is no error
# except ZeroDivisionError:
#     print("Message:Execution is not Successful-divided by zero is not possible")
# except IndexError:
#     print("Message:Execution is not Successful-index number doesn't exist ")
#
# print("I am here because the exception is handled or there was no exception")
#
#####Note: In above code there was an index error and handled by two exceptions ZeroDivisionError and IndexError
# # ZeroDivisionError is not relivent but IndexError exception could handled it so it's message is printed
# # As program is not terminated so in next step found print statement which was printed
#
## finally keyword-->whether exception is handled or not finally block will be executed
######Please Comment out to execute following code
# try:
#     list1 = [20, 0, 10]
#     result1 = list1[0] / list1[2]  # there is no [3]->IndexError: list index out of range
#     print(result1)
#     print("Execution Successful") # It will be printed if there is no error
# except ZeroDivisionError:
#     print("Message:Execution is not Successful-divided by zero is not possible")
# finally:
#     print("You can see me all the time. ->exception/no exception ->handled/not handled")

#####Note: In above code print statement of finally block is executed all the time whether the exception is handled or not
# It will be executed there is an exception or not.
# Show must go on

## Multi exception handling by using (exception,exception)
######Please Comment out to execute following code
# try:
#     num1=int(input("Enter 1st int Number: "))
#     num2=int(input("Enter 2nd int Number: "))
#     result=num1/num2
#     print("Result:",result,end=" (Entered correct input ")
# except (ValueError,ZeroDivisionError):
#    print("(Couldn't calculate, Entered incorrect input. Try Again",end="")
# finally:
#     print("-Thanks)")

## Using raise keyword in exception handling---handle the exception and print the message
######Please Comment out to execute following code

# def voter(age):
#     if age<18:
#         raise ValueError ("Invalid Voter")
#     return "Go Ahed! No objection with age"
#
#
# #calling the function
# age=int(input("Enter voter's age: "))
# checkAge=voter(age)
#print(checkAge)

#### Note: raise keyword is used explicitly throw an exception-->raising ValueError
# raise can handle the exception but can't let you go for next step-->Thanks! is not printing
# see the following code

######Please Comment out to execute following code
# age = int(input("Enter voter's age: "))
# if age < 18:
#     raise ValueError("You are not valid voter")
# else:
#     print("Go Ahed! No objection with age",end="")
#
# print("-Thanks!")


# if we use try-except block with raise then after handling exception it will go for next step
# print next step message
# this time message will be different
def voter(age):
    if age<18:
        raise ValueError ("You are not valid voter")
    return "Go Ahed! No objection with age"


#calling the function
age=int(input("Enter voter's age: "))
try:
    checkAge=voter(age)
    print(checkAge)
except ValueError as e: # we are putting error in e
    print(e) # it was "You are not valid voter"-->will printed same

print("-Thanks!")

