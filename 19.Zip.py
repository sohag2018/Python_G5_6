# By using Zip we can combine multiple lists in a single list

#let's take two lists:
id=[101,102,103,104,105,106]
name=["Monir","Tofayel","Sharif","Sohag","Lobid","Orfat"]
address=["Jamaica", "Manhattan", "Woodside","Woodside","LongIsland","VA"]
# our target is making a list like-->[(101, Monir, Jamaica),(),().....]-->in some Tuples ()
#Syntax-->zip(list, list)--->to put in new list--type cast with list

member=list(zip(id,name,address))
print("<<<<<<<single value>>>>>>>>>>>>>>")
print(member[0])

print("<<<<<<<<all value>>>>>>>>>>>>>>>>>")
print(member)

print("<<<<<<all value  iteration>>>>>>>>")
for x in member:
    print(x)

print("<<<<<distribute from zip func>>>>>")
print(list(zip(name,"123456")))


