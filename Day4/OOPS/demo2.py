print("Demo for the Classes and Objects")

class Employee:         # class creation

    def __init__(self,id,name):
        self.id = id
        self.name = name

    def display(self):     # self represents the current object/instance
        print('Inside display method')
        print('The Id is',self.id)
        print('The Name is:',self.name)

print('This is the example for class and object')
print("Creating the Objects..")
emp = Employee(101,'Rohit')      # object creation
print('Printing the Details of Object')
print(emp.id)
print(emp.name)
print("Calling the Display Method")
emp.display()
emp1 = Employee(102,'Virat')
print("Calling the Display Method for 2object")
emp1.display()

