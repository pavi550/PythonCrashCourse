# Class Methods

class student:
    counter = 0
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        student.counter = student.counter+1

    def msg(self):      # takes object instance
        print(self.name,'-- got --',self.marks)

    @classmethod
    def grades(cls,name,marks):     # cls takes class
        return cls(name,((marks/600)*100))

print('Demo for the Class method')
s1 = student('Rohit',89)
s2 = student('Amit',92)
print("The objects are created..")
print("Calling the method msg")
s1.msg()
s2.msg()

#instead of grade we are available with total marks and need to calculate the grades
total = 550
name = 'Ria'
marks = ((total/600)*100)  # we calculate the grades
s3 = student(name,marks)
print(s3.marks)
s3.msg()
total = 590
name = 'Anand'
s4 = student.grades(name,total)
print(s4.marks)
s4.msg()

