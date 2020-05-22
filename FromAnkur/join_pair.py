## how to join pair of elements of list

# Initialising list
list1 = ['a', 'b', 'c', 'd', 'e', 'f']

# Printing initial list
print("Initial list", str(list1))
print(list1[::2])  # same 0::2 -->starts from 0   :: 2 -> means every 2nd
print(list1[1::2])  # starts from 1   :: 2-->every 2nd
# Pairing-->using zip()
result = [i + j for i, j in zip(list1[::2], list1[1::2])]

# Printing final result
print("Result", str(result))

# (2) list comprehension
# Pairing the elements of lists
result1 = [list1[i] + list1[i + 1] for i in range(0, len(list1), 2)]

# Printing final result
print("Result", str(result1))

# (1) consecutive elements' summation pair--> Using loop
list2=[1,2,3,4,5,6,7,8] # total elements should be even number
print("Original list:",list2)
res = []
for e in range(0, len(list2), 2):
    res.append(list2[e] + list2[e + 1])

# Printing result
print("Pair summation of list : " + str(res))

#         problem
# #(2)# zip() + list comprehension
# res = [i + j for i, j in zip(list2, list2[1:])[::2]]
#
# # Printing result
# print("Pair summation of list : " + str(res))