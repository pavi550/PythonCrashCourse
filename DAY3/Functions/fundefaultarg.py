#Default argument function

def display(name = 30, age = "Rohit"):  # default arguments
    print("The name of the student is ",name)
    print("The age of the student is ",age)

print("The demo for Default argument Function")
# taking values from the user
a = str(input("Enter the name: "))
b = int(input("Enter the age: "))
print("A:",a)
print("B:",b)
# printing the details
print("Calling the function")
display(a, b)
print("***********************"*2)
print("Calling the function with 1 argument")
display(a)
print("***********************"*2)
print("Calling the function without arguments")
display()
print("***********************"*2)
print("Calling the function with 1 argument")
display(int(b),)
print("The code ended...")
