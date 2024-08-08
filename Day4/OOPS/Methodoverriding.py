# Method overriding

import math
# Super class
class Polygons:
    def number_of_sides(self):
        return 0
    def area(self):
        return 0
    def perimeter(self):
        return 0
# Triangle class inherits from Polygons
class Triangle(Polygons):
    def number_of_sides(self):
        return 3
    def area(self, base, height):
        return 1 / 2 * base * height
    def perimeter(self, a, b, c):
        if a + b > c:
            return a + b + c
        else:
            return "Invalid input: make sure a + b > c"


tri = Triangle()
print("Triangle Area:", tri.area(15, 25))
print("Perimeter:", tri.perimeter(15, 20, 25))
print("-----------------")
print("Calling the area method from Polygon class")

