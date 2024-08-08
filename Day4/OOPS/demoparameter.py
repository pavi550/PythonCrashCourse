class product:
    'This class is for parametorized constructor demo'
    def __init__(self,name):
        self.name = name
        print('This is a parameterized constructor')

    def method1(self,name):
        print('This is inside the class')
        print('The name is:',self.name)

print("Crearting the objects")
a1 = product('Soap')
print('Calling the method')
a1.method1(a1.name)
print("Crearting the object 2")
a2 = product('Car')
a1.name = 'Cricket-Bat'    # updating the instance variable
print(a1.name)
print('Calling the method')
a1.method1(a1.name)

