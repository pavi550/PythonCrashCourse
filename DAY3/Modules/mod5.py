# importing mod1 here in mod2

# import mod1    # here main method gets executed from mod1
from mod3 import displayMsg

def displayMsg():
    print("This is function from Mod2")
    print("Welcome to python modules....")
print("Demo 1 for Modules")
print("Lets import the files..")
displayMsg()
print("Inside Mod2.The code ended....")

from mod3 import displayMsg
print("Imported the module mod")
# displayMsg()
displayMsg('Virat')
displayMsg('pr')
displayMsg('Virat')   # trying to call function from mod1
