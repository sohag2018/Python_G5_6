#1. Hierarchical , 2. Multi-level, 3. Multiple Inheritance

#Multiple
class A:
    def display(self):
        print("I am from A class")

class B():
    def display(self):
        print("I am from B class")

class C(A,B): # Multiple Inheritance
    pass

c1=C()
c1.display() #-->If same method in both class then first one will be prefred


