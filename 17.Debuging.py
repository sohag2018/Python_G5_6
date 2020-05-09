#addition cal function:
def add(*numbers):
    sum=0
    for num in numbers:
        sum=sum+num
    return sum

#call the function
print(add(5,10,20)) #output: 35

##How does the above program work?---> when func (Line-9) is called arguments are being passed-->line-2 and stored in numbers Tuples as a container
# Now it goes next step of the program line 6 (out of the boundary of for loop) and returns current value of sum=35

#In line-9: function is calles and passed the values to be added---->control goes to line-2
#In Line-2: all values are stored in numbers Tuples (like a container)---->control goes to line-3
#In Line-3: sum value is 0, no actions found---->control goes to line-3
#In Line-4: For looping purpose values are put in num variable. in this line after first traversing found num value 5--->control goes to line-5
#In Line-5: num value is added with prev. sum value (0+5=5) as a result sum value in line-3 becomes 5--->control goes to line-4
#In Line-4: this time num value is 10--->control goes to line-5
#In Line-5: num value is added with prev. sum value (5+10=15) as a result sum value in line-3 becomes 15--->control goes to line-4
#In Line-4: this time num value is 20--->control goes to line-5
#In Line-5: num value is added with prev. sum value (15+20=35) as a result sum value in line-3 becomes 35--->control go to line-4
#In Line-4: this time no more values->looping is over-->control goes to line-6
#In Line-6: function returns the curent sum value 35 which is stored in line 3-->control goes to line-9 and print sum value 35
## next program debging finds the where is actul problem
#addition cal function:
def add(*numbers):
    sum=0
    for num in numbers:
        sum=sum+num
        return sum

#call the function
print(add(5,10,20)) #output: 5 but expected 35 what happened see debuging details

##
#In line-34: function is calles and passed the values to be added---->control goes to line-27
#In Line-27: all values are stored in numbers Tuples (like a container)---->control goes to line-28
#In Line-28: sum value is 0, no actions found---->control goes to line-29
#In Line-29: For looping purpose values are put in num variable. in this line after first traversing found num value 5--->control goes to line-30
#In Line-30: num value is added with prev. sum value (0+5=5) as a result sum value in line-28 becomes 5--->control goes to 31
#In Line-31: function returns the curent sum value 5 which is stored in line 28-->control goes to line-34 and print sum value 5

#Findings: return statement supposed to be out of the for loop boundary.
#As it was inside the for loop function ends looping and returns the current sum value after first traversing