# Logical Operator--> And, or , not  --when we use more than one conditions
# To make program: Largest/Smallest number,  Leap year, Vowel/consonent, Capital/small
num1=90
num2=10
num3=80
if num1>num2 and num1>num3:print(num1)
elif num2>num1 and num2>num3:print(num2)
else:print(num3)

#Vowel
myAlphabet =input("Enter any alphabt: ")
if myAlphabet=='a'or myAlphabet=='e'or myAlphabet=='i'or myAlphabet=='o'or myAlphabet=='u':
    print(myAlphabet, "is a Vowel")
else:print(myAlphabet,"is a Consonent")

#Letter grade
marks=int(input("Monir vai pleae Enter your marks: "))
if 80<=marks<=100:print("A+")
elif marks>=70 and marks<=79: print("A")
elif marks>=60 and marks<=69: print("-A")
elif marks>=50 and marks<=59: print("B+")
elif marks>=40 and marks<=49: print("B")
else:print("F")

