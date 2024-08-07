# reading multiple inputs from user

a,b = [int(a) for a in input('Enter two values:').split()]
print('First number is:',a)
print('Second number is:',b)
print('******'*10)
a,b,c = [int(a) for a in input('Enter three values:').split()]
print('First number is:',a)
print('Second number is:',b)
print('Third number is:',c)

