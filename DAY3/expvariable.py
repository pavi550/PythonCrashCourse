#The except statement using with exception variable

try:
    x = int(input('Enter the first number: '))
    y = int(input('Enter the second number: '))
    print (x/y)
except (ZeroDivisionError, TypeError, NameError)as e:
    print("This is Zero division error ",e)
except Exception as e:
    print(e)
print("Program ended")
