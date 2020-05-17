#Creating a class


#Need to know about constructor using rules----->
'''Unlike Java, you cannot define multiple constructors.
However, you can define a default value if one is not passed.'''

class Students: #syntax of creating class
    id=""
    name=""
    gpa=""
    # def __init__(self):
    #     print("default cons")
    def __init__(self,id,name,gpa):
        self.id=id
        self.name=name
        self.gpa=gpa
        print(id,name,gpa)


class Employees:
    pass

#creating an object of Students class
#Students st1=new Students()
#st1=Employees()
#st1= Students() # func starts with lower case but class upper case
# print(isinstance(st1,Students)) # True if obj creation is ok
# print("............................................")
# st1.id=101
# st1.name="Mohammad Tofayel"
# st1.gpa=5.00

st11=Students(505,"Lobid",101)
#st12=Students(506,"Lob")





# print(f"ID:{st11.id},Name:{st11.name}GPA: {st11.gpa}")
# print("\n............................................")
#
# st2=Students()
# st2.id=102
# st2.name="Mohammad Sohag"
# st2.gpa=4.99
# print(f"ID:{st2.id},Name:{st2.name},GPA:{st2.gpa}")
# print("\n............................................")
#
# st3=Students()
# st3.id=105
# st3.name="Mohammad Monir"
# st3.gpa=5.00
# print(f"ID:{st3.id},Name:{st3.name},GPA:{st3.gpa}")