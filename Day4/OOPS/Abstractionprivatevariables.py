# Abstraction , private variables
class class1:
    __count = 0   # variable with double underscore is private varaible
    pi = 3.14
    def __init__(self):
        class1.__count = class1.__count+1

    def display(self):
        print('The number of objects are',class1.__count)

print('demo for private Variable')

c1 = class1()
c2 = class1()
print('Objects Created.')
print("Calling the display method..")
c2.display()
print("Getting the value of pi for c2")
print(c2.pi)
print("Getting value of __count for c2")
#print(c2.__count)  # gives error attribute not present
#print('Getting the Count of Objects',class1.__count)  # gives error attribute not present
print("Creating a private instance variable")
c2.__count = 4    # this is private instance variable
print("The value for c2.__count :",c2.__count)

