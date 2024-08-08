# Multiple constructors

class class1:
    " Demo for multiple constructors in python"
    def __init__(self,name,id,age):   # constructor2
        self.name = name
        self.id = id
        self.age = age
    def __init__(self,name,id):    # constructor1
        self.name = name
        self.id = id
    def __init__(self):
        print("This is constructor 3")

c1 = class1()
print('This is a constructor demo')
print("Creating the object c2")
c2 = class1('Name1',121)
print("Creating the object c3")
c3 = class1('Rohit',222,34)
print("Creating the object c1")


#
# print("Creating the object c3")
# c3 = class1('Rohit',222,34)
# print("Creating the object c1")
# c1 = class1()
# print("Creating the object c2")
# c2 = class1('Name1',121)
# print('This is a constructor demo')

# constructor overloading is not supported in python'
# latest definition of the constructor available for the interpreter will be utilised'

