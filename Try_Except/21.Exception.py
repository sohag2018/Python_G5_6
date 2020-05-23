#Exception-->Runtime error
num=int(input("Enter a number: "))
result=20/num
print(result)
print("Execution Successful") # It will be printed if there is no error

# #1. exception due to type mismatch
# num1=input("Enter a number: ")
# result1=20/num1 #trying to devide int by string->show runtime error
# print(result1) #->output:TypeError: unsupported operand type(s) for /: 'int' and 'str'
# print("Execution Successful") # It will be printed if there is no error

#2. exception due to illogical operational attempt
num2=int(input("Enter zero: "))
result2=20/num2 #if zero entered-->which will be illogical operational command/ cant devide by zero
print(result2)
print("Execution Successful") # It will be printed if there is no error

#3. exception due to non existant content request
text="Sohag"
print(text[0]) #exist--S
print(text[-1]) #exist--g
print(text[5]) # doesnt exist-->IndexError: string index out of range




