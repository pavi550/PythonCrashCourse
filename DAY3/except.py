#The except statement with no exception

try:
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    c = a/b
    print("The result is:",c)
except:
    print("Can't divide with zero")

else:
    print("This is else block..")
print("\ncode ended..")
