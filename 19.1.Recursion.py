#Recursion-->function is called by itself--->we need to stop the call otherwise it will go for infinite time
#to stop the process need to use base case--condition
#-->when we find factorial of any number-->5!=5*4*3*2*1-->n!=n*(n-1)!--->base case is 1

# create a recursive function
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

print(fact(5))

#Explanation->
# In Line 12: function is called and 5 is passed as n-value-->controls goes to Line 6
# In Line 6: replace value of n-->controls goes to Line 7
# In Line 7: condition false 5 not equal to 1-->controls goes to Line 10
# In Line 10: 5 is multiplied by what fact(5-1) returns-->controls goes to Line 6
# In Line 6: replace value of n by 4-->controls goes to Line 7
# In Line 7: condition false 4 not equal to 1-->controls goes to Line 10
# In Line 10: 4 is multiplied by what fact(4-1) returns-->controls goes to Line 6
# In Line 6: replace value of n by 3-->controls goes to Line 7
# In Line 7: condition false 3 not equal to 1-->controls goes to Line 10
# In Line 10: 3 is multiplied by what fact(3-1) returns-->controls goes to Line 6
# In Line 6: replace value of n by 2-->controls goes to Line 7
# In Line 7: condition false 2 not equal to 1-->controls goes to Line 10
# In Line 10: 2 is multiplied by what fact(2-1) returns-->controls goes to Line 6
# In Line 6: replace value of n by 1-->controls goes to Line 7
# In Line 7: condition true 1 equal to 1-->controls goes to Line 8
# In Line 8: returns 1-->found the base case process is stopped    #            5*4*3*2*1
