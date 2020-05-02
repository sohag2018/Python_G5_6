#(1)
marks=75
if marks>=40:
    if marks>=80:print("distinct")
    elif marks>=75:print("Excellent")
    else:print("general")
else:print("Fail")

#(2)
num1=30
num2=20
num3=-40

if num1>num2:
    if num1>num3:print(num1)
    else:print(num3)
if num1<num2: #else:-->we could use else here too
    if num2>num3: print(num2)
    else:print(num3)
