## Consecutive K elements join in List
# using List comprehension

# Initializing list
list1 = ['1', '2', '3', '4', '5']

# printing original list
print("The original list is : " + str(list1))

# Initializing K/consecutive
con = 2

# Consecutive K elements join in List
# using List comprehension
result = ["".join(list1[idx: idx + con]) for idx in range(len(list1) - con + 1)]

# printing result
print("List after consecutive joining : " + str(result))

#2 : Using loop
result1 = []
for idx in range(0, len(list1) - con + 1):
    result1.append("".join(list1[idx: idx + con]))

# printing result
print("List after consecutive joining : " + str(result1))