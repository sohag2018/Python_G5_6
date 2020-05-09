from Module.ModuleArea import*
# Problem: Mr. Lobid has two gardens in bronx and Long Island. Both gardens are ractangle shaped and almost same size
# He wants to make sure actual which garden is bigger and how big.
# Find the area of both gardens and help him to figure out which garden is big and how big,
# when length and width found as follows.
#Bronx Garden: L=10 ft, H=7.5 ft  and Long Island Garden: L=9.5 ft , H=8 ft

#Bronx Garden:

bGA=ractangleCal(10,7.5)
print(bGA)
lGA=ractangleCal(9.5,8)
print(lGA)

big=compareArea(bGA,lGA)
print("Big One is:",big)



