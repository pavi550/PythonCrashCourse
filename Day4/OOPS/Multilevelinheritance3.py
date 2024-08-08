print('Demo for Multiple Inheritance')
'both base classes have same methods..'
class Class1:
    def func2(self):
        print('This is the func2 method from Class1')

    def func4(self,name):
        print('This is the func4 from Class1')
        print('The name is',self.name)
print("Class 1 created")
class Class2:

    def func2(self):
        print('This is the func2 method from Class2')
print("Class 2 created")

class Class4:

    def func2(self):
        print('This is the func2 method from Class4')

class Class3(Class2,Class4,Class1):   # sequence of classes that we inherit
    print('This is class 3')

    def func3(self):
        print('This is the func3 from class 3')

print("Class 3 created")
print("Class 3 is child class for class1 and class 2")
print("Crearting object for class 3")
c3 =Class3()
print('Calling the method from Class1 using C3')
c3.name = 'Rohit'
c3.func4(c3.name)
print('Calling the method from Class2 using C3')
c3.func2()     #

"""
when we do multiple inheritance, and we have same named methods in multiple classes,
then the call to the method will be resolved by the sequence of the base classes you have inherited.
"""

