#Creating a class
class Students: #syntax of creating class
    id=""
    name=""
    gpa=""

#creating an object of Students class
st1= Students() # func starts with lower case but class upper case
print(isinstance(st1,Students)) # True if obj creation is ok
print("............................................")
st1.id=101
st1.name="Mohammad Tofayel"
st1.gpa=5.00

print(f"ID:{st1.id},Name:{st1.name}GPA: {st1.gpa}")
print("............................................")

st2=Students()
st2.id=102
st2.name="Mohammad Sohag"
st2.gpa=4.99
print(f"ID:{st2.id},Name:{st3.name},GPA:{st3.gpa}")

st3=Students()
st3.id=102
st2.name="Mohammad Sohag"
st2.gpa=4.99
print(f"ID:{st2.id},Name:{st2.name},GPA:{st2.gpa}")