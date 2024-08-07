# Variable values inside and outside function

def func1():
    print('This is the function')
    a = 20
    print('Inside the function',a)


print('This is the demo for Functions')
print('This is the 2nd statement')
func1()
a = 35
print('Outside the function',a)
func1()
