# Class Variables
print("Demo for the class variable...")
class Circle:
    pi = 3.14			#class variable
    def __init__(self):
        self.radius = 1

    def area(self):
        return self.radius * self.radius * Circle.pi

print("Creating the Objects")
c = Circle()
print("Creating the instance variable")
c.radius = 3       # instance variable
print("Calling the Area method")
print(c.area())
print("trying to access the class variable")
print(Circle.pi)
print("Updating the class variable")
Circle.pi = 4
print("Updated class variable :",Circle.pi)

