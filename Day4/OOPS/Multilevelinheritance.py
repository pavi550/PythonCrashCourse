# Multilevel inheritance
class Base:      # Parent class1
    def func1(self):
        print('This is the func1 from Base class')

class Derived(Base):     #child class for Base class
    print('This is the child class')

    def func2(self):
        print('This is the function 2 in Derived class')
print('Demo for  Multi-level Inheritance')
d1 = Derived()
print("Object of Derived class created..")
print('Calling the Base class function')
d1.func1()
print('Calling the Derived class function')
d1.func2()

class Child(Derived):    #child class for Derived class
    print('This is the Child class')

    def func3(self):
        print('This is the function from Child class')
print("Chile class created..")
print("Creating the object of child class")
c1 = Child()
print('Calling the Derived class function using C1')
c1.func2()
print('Calling the Base class function using C1')
c1.func1()

