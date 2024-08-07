#The catching multiple Exceptions in single block
try:    
    a = int(input("Enter a:"))    
    b = int(input("Enter b:"))    
    c = a/b;    
    print("a/b = %d"%c)    
except (ZeroDivisionError, TypeError, NameError) as e:    
    print("can't divide by zero ",e) 
   
else:    
    print("This is the else block")
