# Keyword argument demo

# defining the function
def display(a=18, b="Rohit"):   # default arguments
    print("The name of the student is %s", a)
    print("The age of the student is %d", b)

print("Function to get student details and print it..")
# taking values from the user
name = str(input("Enter the name: "))
age = int(input("Enter the age: "))

# printing the details
print("Calling the function with arguments")
display(name, age)
display("Suresh")
print("Calling the function with 1 argument")
display(age)   # 1st positional argument
# print("Calling the function without arguments")
# display()
print("Calling the function with keyword arguments")
display(b="anand", a=25)
print("Calling the function with 1 keyword arguments")
display(b=name)

