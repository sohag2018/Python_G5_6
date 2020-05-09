#Method Overriding-->using func from parent class with same name but changing the value

#In this program we will after inheritance chile class automatically get access the constrcuctor
# when we will create the obj means we will call the constructor
# we will pass keyord to avoid the restriction to create fun/cons in class

class Nokia:#Parent class
    #constructor
    def __init__(self):
        print("I am in Nokia class")

class Samsung(Nokia): #Sub class---inherits Nokia class
    pass # You need to create at lease one func/cons--->to avoid we used pass
#create obj
#there is no constructor of Samsung class but....
s1=Samsung()

