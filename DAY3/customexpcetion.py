# Custom Exception

class ErrorInCode(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)

try:
    age = int(input("Enter the age:"))
    if(age<18):
        raise ErrorInCode("Plz enter valid age")
    else:
        print("the age is valid")
except ErrorInCode as e:
    print("The age is not valid",e)
