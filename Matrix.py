matrix=[
    [1,2,3],
    [4,5,6]
]

print(matrix[-1][-1])# last / [1][2]
print(matrix[1][2])

#print with inner for loop
for row in matrix:
    for col in row:
        print(col)
