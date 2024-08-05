import sys

def add (num1,num2):
    sum=num1+num2
    return sum

def sub(num1,num2) :
    sub=num1-num2
    return sub

def mul(num1,num2):
    mul=num1*num2
    return mul

def div(num1,num2) :
    div=num1/num2
    return div


num1=float (sys.argv[1])
operation=sys.argv[2]
num2=float(sys.argv[3])

if operation=="add" :
    output=add(num1,num2)
    print(output)
elif operation=="sub" :
        result=sub(num1,num2)
        print(result)
elif operation =="mul" :
    result=mul(num1,num2)
    print(result)
else :
    result=div(num1,num2)
    print(result)
