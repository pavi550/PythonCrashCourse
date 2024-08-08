# Class Variables
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
print("trying to access the class variable")
print(Circle.pi)
print("Printing the value of pi for object c")
print("Pi for c:",c.pi)   #
print("Updating the class variable")
Circle.pi = 4
print("Updated class variable :",Circle.pi)
print("Printing the value of pi for object c")
print("Pi for c:",c.pi)   #
print("can we reassign the pi for object C?")
c.pi = 6       # pi here is now instance variable for object c
print("Updates Pi for c:",c.pi)   #
print("Calling the Area method")
print(c.area())
print("trying to access the class variable")
print(Circle.pi)

