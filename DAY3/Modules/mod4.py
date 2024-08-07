# importing mod3 here in mod4

import mod3    # here main method gets executed from mod1
# from mod3 import displayMsg

def displayMsg():
    print("This is function from Mod4")
    print("Welcome to python modules....")
print("Demo 1 for Modules")
print("Lets import the files..")
mod3.displayMsg('Rohit')
print("Inside Mod4.The code ended....")

# def displayMsg():
#     print("This is function from Mod2")
#     print("Welcome to python modules....")
displayMsg()
mod3.displayMsg('Virat')   # trying to call function from mod1
displayMsg()