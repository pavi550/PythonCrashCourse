# Operator Overloading
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __add__(self, other):  # p3 = p1+p2 [(x3,y3)= (x1+x2),(y1+y2)]
        # operand + operand2
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)   #returning object of class Point

p1=Point(2,3)
print('This are the x and y co-ordinates of P1')
print(p1)
p2=Point(3,7)
print('This are the x and y co-ordinates of P2')
print(p2)
print('Adding two points using operator overloading')
p3=p1+p2 # p3 = p1+p2 [(x3,y3)= (x1+x2),(y1+y2)]
print('After addition the new point is- ',p3)

