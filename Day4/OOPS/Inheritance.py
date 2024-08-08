# Inheritance
print('Demo for Inheritance')
class Parent1:
    'This is the parent class with display method'
    def display(self):
        print('This is display from Parent')
print("Parent 1 class created")

class Child(Parent1):   # inheriting the Parent1 class
    'Child class for Parent1'
    def __init__(self,name):
        self.name = name

print("Child class created")
print("Creating the object of child class")
c1 = Child('Rohit')
print("Object created...")
print("Name of the Child is:",c1.name)
print("Accessing the Method from Parent1 class")
c1.display()

