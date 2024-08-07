#python function to print student details (Keyword argument)
def display(a,b):   # Keyword arguments
    print("The name of the student is ", a)
    print("The age of the student is ", b)

print("Function to get student details and print it..")
# taking values from the user
name = str(input("Enter the name: "))
age = int(input("Enter the age: "))
print("***********************"*2)

print("Calling the function with keyword arguments")
display(b=25, a='Virat')  # keyword argument
print("***********************"*2)

print("Calling the function with keyword and positional argument")
display(23,b=24) # some arguments are keyword and some are not
print("***********************"*2)

# 23 is considered as positional argument and value goes to a
print("Calling function with proper values")
display('Rohit',20)
print("***********************"*2)

print("calling function with postional arguments after keyword argument")
#display(b=20,'Rohit')  # positional arguments should be written fist
# display("Rohit',b=20)

