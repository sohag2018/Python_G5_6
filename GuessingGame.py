import random
# or we could: from random import randint

win=0
lost=0

for i in range(1,6):
    userNumber = int(input("Enter any number from 1 to 5: "))
    actulNumber = random.randint(1, 5)
    if userNumber==actulNumber:
        print("You Won")
        win=win+1
    else:
        print("You Lost, It was",actulNumber)
        lost=lost+1
print("Result in 5 attempts: ","You Won:",win,"& You Lost:",lost)