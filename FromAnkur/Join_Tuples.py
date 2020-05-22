# joining tuple elements
# (1) using join() + list comprehension

# initializing tuple list
list1 = [('Sohag', 'Orfat', 'Manir'), ('Tofayel', 'Sharif', 'Lobid')]

# printing original list
print("The original list is : " + str(list1))

# using join() + list comprehension
# joining tuple elements
result = [' '.join(t) for t in list1]

# printing result
print("The joined data is : " + str(result))

# (2)Using map() + join()
# joining tuple elements

# #using map()-->accepts parameter join and list obj -->then typcast to list
result1 = list(map(" ".join, list1)) #1st param key, 2nd param value

# printing result
print("The joined data is : " + str(result1))
