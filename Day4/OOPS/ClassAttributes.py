# Class Attributes

class stud:
    'This is the student class and this demo is for Attributes'
    def __init__(self,id,name,age):
        self.id = id
        self.name = name
        self.age = age
print("Class student created..")
print("Creating the objects")
s1 = stud(121,'Rohan',21)
s2 = stud(123,'Sumit',20)

print('Demo for class Attributes')
# getting the value using getattr
print('The name is: ',getattr(s1,'name'))

# Setting the value for an attribute
print('New value for Name',setattr(s1,'name','Supriya'))

# getting the value using getattr
print('The name is: ',getattr(s1,'name'))

# deleting the attribute
print('Deleting an Attribute:', delattr(s1,'id'))

# Checking the attribute
print('Is Id present? -',hasattr(s1,'id'))

print('The Dict is:',s1.__dict__)
print('The Module is:',s1.__module__)
print('The DOcumentation is:',s1.__doc__)

