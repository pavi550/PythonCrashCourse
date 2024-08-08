print("Demo for the Classes and Objects")

class Employee:         # class creation
    'Demo for default constructor...'
    id = 1001   # id = None
    name = 'Anand'

    def display(self):     # self represents the current object/instance
        print('Inside display method')
        print('The Id is',self.id)
        print('The Name is:',self.name)

print('This is the example for class and object')
print("Creating the Objects..")
emp = Employee()      # object creation
print('Printing the Details of Object')
print(emp.id)
print(emp.name)
print("Calling the Display Method")
emp.display()
emp2 =Employee()
print(emp2.id)
print(emp2.name)
print("Updating the data for emp2")
emp2.id = 1002
emp2.name = 'Rohit'
print("Calling the display method")
emp2.display()
