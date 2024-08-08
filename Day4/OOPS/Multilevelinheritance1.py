print('Demo for Multiple Inheritance')
class Class1:
    def func1(self):
        print('This is the method fron Class1')
    def func3(self,name):
        print('This is the func2 from Class1')
        print('The name is',self.name)
print("Class 1 created")
class Class2:
    def func2(self):
        print('This is the method from Class2')
print("Class 2 created")

class Class3(Class1,Class2):
    print('This is class 3')

    def func3(self):
        print('This is the func3 from class 3')

print("Class 3 created")
print("Class 3 is child class for class1 and class 2")
print("Crearting object for class 3")
c3 =Class3()
print('Calling the method from Class1 using C3')
c3.func1()
print('Calling the method from Class2 using C3')
c3.func2()     # error in o/p missing 1 argument name
#
# print(isinstance(c3,Class2))
# print(isinstance(c3,Class3))
# print(issubclass(Class2,Class1))
# print(issubclass(Class3,Class1))

