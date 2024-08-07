# gobal keyword example
# scope of variable when declared at program level(global)
# use of global keyword
# use global variable inside function such that i can modify it
x ='Python'

def func1():
    global x
    print('The value of x', x)
    a = 'local'
    x = x*2        # since we have used global keyword
    print('The value of x', x)
    print('The value of a', a)

print('This is ouside function')
func1()
print('X outside the funct',x)

#print('The value of a', a)
