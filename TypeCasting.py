#(1)--before typcasting
# num1=input("Enter First Number: ") #5
# num2=input("Enter Second Number: ")#5

# result=num1+num2
# print("Before typcasting "+result)#output will be 55 because as string it is concatenated
# (2)---after typcasting
# result2=int(num1)+int(num2)
# print("After typcasting ",result2)#output will be 10 because after typcasting both numbers are int AND need to use (comma) not (plus)

#(3) typcast with the input function
num1=int(input("Enter First Number: ")) #5
num2=int(input("Enter Second Number: "))#5

result=num1+num2
print(result)
