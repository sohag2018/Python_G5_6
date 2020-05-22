#Tuples--> similar data structure to List but it is immuteable we cant change it's value but we can change list's value

#Creating Tuples-->have a variable then put the values in parenthesis ()
#students=("Sohag","Sharif","Orfat", "Tofayel")

students=(("Sohag",41,"Woodside"), "Orfat", "Tofayel")
#If we try to change:-->Once Tuples create we cant assign new value even in new index
#students[1]="Palash" # will show-->TypeError: 'tuple' object does not support item assignment
print(students)
#Print:
print(students[0])
print(students[-1]) #last index value

# print-->slicing
print(students[1:]) # output-->('Sharif', 'Orfat', 'Tofayel')

#print-for loop
for i in students:
    print(i)

