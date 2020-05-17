
# Let's create the main func and put the print statement there
def welcome():
    print("Hello!")
    print("Welcome you all")

def seeOff():
    print("Good Bye")

seeOff()
# we want to execute our specific code only in this module (from othe module we can import this module as a library)
#let's put the condition not to be executed in fourth module
if __name__ == "__main__":
    welcome()



## now go to Fourth module and import third module there and run