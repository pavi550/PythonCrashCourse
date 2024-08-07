#The program with multiple Exceptions
try:    
    a = int(input("Enter a:"))    
    b = int(input("Enter b:"))    
    c = a/b;    
    print("a/b = %d"%c)    
except ZeroDivisionError:    
    print("can't divide by zero") 
except TypeError:    
    print("This is type error")    
else:    
    print("This is the else block")   

