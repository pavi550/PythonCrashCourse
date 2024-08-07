# Handling the Error with try except block

try:
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    c = a/b
    print("The result is:",c)
except:
    print("Can't divide with zero")
