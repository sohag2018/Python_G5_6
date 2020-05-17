'''--->The try block lets you test a block of code for errors.

---->The except block lets you handle the error.

--->The finally block lets you execute code, regardless of the result of the try- and except blocks.'''


#Exception Handling:

#(1): Trying to print x without assigning any value for it

#What happen if we dont handle the exception:
'''y=5
print(x) 
print(y)
#Without the try block, the program will crash and raise an error:
#It will give:---> NameError: name 'x' is not defined
# It will not print y value though value was assigned

'''

#What happen if we use try---except:
y=5
try:
    print(x) #We didnt assigned value for x
except:print("An exception occured")
print(y)
#when try block fails and raises error then control goes to except blocks and print "An exception occured"
# Then control goes for other steps and print y value


#Many Exceptions:can define as many exception blocks as we want
#Print one message if the try block raises a NameError and another for other errors
print("#Many Exceptions Blocks----------------------")
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

print("## Else Block:---------------------------------")
#to define a block of code to be executed if no errors were raised
#In this example, the try block does not generate any error:
try:
  print("Sohag")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

#Try block is good to be executed--no error in try block
# so nothing to do in except block
# else  block got executed


print("## Finally Block------------------------------")

try:
  print(x)
except:
  print("Variable is not defined")
finally:
  print("print me no matter what")
#x varibale is not defined-->try block raises error
# except block--> handled the exception and print message
#finally block--> executed regardless if the try block raises an error or not


print("## Close objects and clean up resources--------")
try:
  f = open("Test.txt")
  f.write("Sharif is a quick learner")
except:
  print("file not found")
finally:
    print("if file is open then close it")
    # f.close()
    # print("File is closed now")

  #In try block we are trying to open Test.txt file by using open() but as file doesnt exist it goes to except block
  # in except bock it will print "file not found"
  # as finally blocks always gets executed so it will print the message then close the file
  # as f is not defined so thrrow an error at last

print("## Raise an exception--->raise keyword----------------")
#
# #Raise an error and stop the program if x is lower than 0:
# x = -1
# if x < 0:
#   raise Exception("Sorry, no numbers below zero")
# '''Output: raise Exception("Sorry, no numbers below zero")
# Exception: Sorry, no numbers below zero'''
#
# # as we raised the Exception message "Sorry, no numbers below zero"
# # so it is printingn Exception: Sorry, no numbers below zero

print("## define what kind of error to raise----------------")
# #define what kind of error to raise, and the text to print to the user
# x = "Sohag"
# if not type(x) is int:
#   raise TypeError("You should enter only int")
#
# '''Output: raise TypeError("You should enter only int")
# TypeError: You should enter only int'''

