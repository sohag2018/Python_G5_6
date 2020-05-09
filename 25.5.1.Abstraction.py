from abc import ABC,abstractmethod
class Shape(ABC):
    def __init__(self,dim1,dim2):
        self.dim1=dim1
        self.dim2=dim2

    @abstractmethod
    def area(self):
        pass


class Triangle(Shape):
    def area(self):
        area=0.5*(self.dim1*self.dim2)
        print("Area of Triangle:",area)

tr1=Triangle(20,30)
tr1.area()

class Ractangle(Shape):
    def area(self):
        area=self.dim1*self.dim2
        print("Area of Ractangle:",area)

rt2=Ractangle(20,30)
rt2.area()


#Note:Why do we use abstruct class--> to use as a blue print / model
# To make a class Abstruct ->need to write (ABC) with the class name like inharitance
# need to import ABC (Abstruct Base Class) from abc module-->need to implement abstructmethod
# need to use annotation before method-->@abstractmethod
# sub class has to use (implement) abstruct method--->gives body
# As Abustruct has at leaset one abustruct method so we can't create obj of it.