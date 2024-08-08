class Base:
    def __init__(self,x):
        self.x = x

class Child(Base):
    def __init__(self,x,y):
        super(Child,self).__init__(x)
        self.y = y

    def print1(self,x,y):
        print('The value for x',self.x)
        print('The value for y ',self.y)

c1 = Child(30,40)
c1.print1(c1.x,c1.y)

