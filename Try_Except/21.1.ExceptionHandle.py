#Exception Handle-->using try block-> for the code and except keyword followed by exception type-> to handle the exception
# #1.block creates ZeroDivisionError exception:
try:
    list=[20,0,10]
    result=list[0]/list[1] #can't divide by zero->ZeroDivisionError
    print(result)
    print("Execution Successful") # It will be printed if there is no error
except ZeroDivisionError:
    print("Message:Execution is not Successful-divided by zero is not possible")

print("I am here because the exception is handled or there was no exception")

# # Note: For exception handle-> need to put the block under try
# # If there is an error code will not be executed->control goes to exception handling block
# # if anything to be printed in exception handling block will be printed
# # As it is handled by the relevent exception type then contro will go for next steps
# # If relevent exception type is not found then program will be terminated there it will not go for next step
#
# #1.block creates ZeroDivisionError exception:
try:
    list1 = [20, 0, 10]
    result1 = list1[0] / list1[3]  # there is no [3]->IndexError: list index out of range
    print(result1)
    print("Execution Successful") # It will be printed if there is no error
except IndexError:
    print("Message:Execution is not Successful-divided by zero is not possible")

print("I am here because the exception is handled with IndexError")
#
# # Note: In the above block problem is about the index and should be handled by IndexError
# # but it was handled by ZeroDivisionError-->program terminated right a way
# # it will not print "Execution Successful" as there is an error in the code and not handled properly
# # it will not print "Message:Execution is not Successful-divided by zero is not possible"
# # it will not print "I am here because the exception is handled or there was no exception"
# # try again just after changing/adding exception type (IndexError)


