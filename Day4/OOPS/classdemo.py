print("Demo for the Classes and Objects")

class circle:
    'This is the first demo for the class'

    def __init__(self, radius):   #Constructor
        self.radius = radius

    def Area(self):     #method
        print('Inside area method')

print("Creating the Objects..")
c1 = circle(5)
print("Object Created..")
print("Calling the Method in the class..")
c1.Area()
print("The Radius of c1 is",c1.radius)
