# Dictionary--->data structure where we can store data in key value pair

studentId={
    "101":"Sohag",
    "102":"Sharif",
    103:"Orfat",    # key-int: value-String
}

print(studentId["101"])  # Sohag
#print(studentId["105"])---->will be shown->KeyError: '105'
print(studentId.get("101")) # Sohag
print(studentId.get(103)) # Orfat

# print all Key's value
for x in studentId:
    print(studentId[x])