# super keyword Demo

class class1:
    def __init__(self,name):
        self.name = name
        print('This is Class1')

class class2(class1):
    def __init__(self,codname):
        print('This is Class 2')
        super().__init__(codname)

class class3(class1):
    def __init__(self,pname):
        print('This is Class 3')
        super().__init__(pname)

class class4(class3,class2):
    def __init__(self,name1):
        print('This is Class 4')
        super().__init__(name1)

c4 = class4('Python')
print('The name is: ',c4.name)

