# Instance Variables
print("Demo for the class variable...")
class Circle:
    pi = 3.14			#class variable
    def __init__(self):
        self.radius = 1

    def area(self):
        return self.radius * self.radius * self.pi

print("Creating the Objects")
c = Circle()
print("Creating the instance variable")
c.radius = 3       # instance variable
print("Calling the Area method")
print(c.area())
c1 = Circle()
print(c1.radius)
print(c1.pi)
print("Creating the instance variable ")
c1.name = 'Circle2' #  instance variable for c1
print("Name of circle is:",c1.name)

