n=input("Enter few numbers using comma: ") #10,20,30,40,50
list=n.split(",") # "10" "20" "30" "40" "50"  ---in split() we need to pass separator , -
print(list[0])
print(list[-1])#last index value
print(list)

#adding:
sum=0
for num in list:
    sum=sum+int(num)
print(sum)


# find out number of letters, words and digit from a sentence

sentence=input("Enter your sentence: ") #My phone number is 3474005813
totalLetters=0
totalWords=0
totalDigit=0

for x in sentence:
    x=x.lower()#to lower case
    if x>='a' and x<='z':
        totalLetters=totalLetters+1
    elif x == ' ':
        totalWords = totalWords + 1
    elif x>='0' and x<='9':
        totalDigit = totalDigit + 1    #  My name
print("total letters: ",totalLetters)
print("total Words: ",totalWords+1)  # Why +1?   My name is Sohag--> space=3, so, words=3+1 (sapce=word logic)
print("total digit: ",totalDigit)





## more example: https://pynative.com