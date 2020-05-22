#Using the property of other class

#class1:
class IPhone:  #-->Base/Super/Parent class
    #function1
    def makeACall(self):
        print("You can make a call")

    # function2
    def sendMessage(self):
        print("You can send Message")

#class2 which inherits IPhone class
class Samsung(IPhone): #-->in() mentioned the class name that is being inherited -->Derived/Sub/child class
    #function3:
    def takesPhoto(self):
        print("You can a take a photo")

#obj creation and call the func
s1=Samsung()
s1.sendMessage() #this func comes from IPhone class
s1.makeACall() #this func comes from IPhone class
s1.takePhoto()

print("------------------------------------------")

#Note: Samusung is sub class and Iphone is Super class-->we can check it by using a func
print(issubclass(Samsung,IPhone)) #True if Samsung is sub class of Iphone


