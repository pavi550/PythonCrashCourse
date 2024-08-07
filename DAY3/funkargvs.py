def func1(age,*name,**kwargs):   #*args   **kwargs
    print('This is the function')
    print('Hello',name)
    print(type(name))
    print(kwargs)
    print((type(kwargs)))
    print("Age is:",age)

print('This is the functions demo')
func1(20,'Rohit',s1=80,s2=70)

# func1('Rohit','Virat')
# func1('Suraj','Latika','Mahesh')
