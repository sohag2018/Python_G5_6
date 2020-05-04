#pattern 1
# *
# * *
# * * *
# * * * *

#
# for i in range(1,6,1):
#     print(i*"* ")

#pattern 2
# * * * * *
# * * * *
# * * *
# * *
# *


# for k in range(5,0,-1):
#     print(k*" *")


#pattern 3

#        * * * * *
#       * * * *
#      * * *
#     * *
#    *


# for x in range(5,1,-1):
#     print((x*" "),(x-1)*"* ")

#pattern 3

#        *
#       **
#      ***
#     ****
#    *****

n2=5
for m in range(n2+1,1,-1):
    print((m*" "),end="")
    for n in range(1,n2,1):
        print(n*"*")


#pattern 4
# *  ---> i*2-1  when i=1-->1*2-1=1
# * * *  ---> i*2-1  when i=2-->2*2-1=3
# * * * *  ---> i*2-1  when i=3-->3*2-1=5

# n1=5
# for j in range(1,n1+1,1):
#         print(((j*2)-1)*"*")


