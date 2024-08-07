# default argument function
def func1(name,str1 = 'This is a good day'):
    print('This is the function')
    print('Hello',name +','+str1)

print('This is the functions demo')
func1('Rohit','Very Good Session...')

func1('Virat')    # when we dont provide the 2nd argument, while execution it takes the default
# from the func definition
