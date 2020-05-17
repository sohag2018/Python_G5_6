# Q: Create a class Triangle. Create two obj of Triangle class. Through constructor pass the value of base and height
# create a function to calculate the area of the triangle with the value passed for. Print the area in console

#Class:
class Triangle:
    base=""
    height=""

    #constructor

    def __init__(self,base,height):
        self.base=base
        self.height=height




    def areaCalculate(self):
        area=0.5*self.base*self.height       #Area=0.5*(base*height)
        return area





#obj
tr1=Triangle(10,5)
area1=tr1.areaCalculate()
print(area1)
print("----------------")
# tr2=Triangle(10,30)
# print(tr2.areaCalculate())