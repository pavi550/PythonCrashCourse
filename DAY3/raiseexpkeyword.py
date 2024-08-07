# raise keyword an be used to call a specific Except block
try:
    age = int(input("Enter the age?"))
    if age<18:
        raise ValueError;
    else:
        print("The age  %a is valid"%age)
except ZeroDivisionError:
    print('This is divide by zero error')

except NameError:
    print('This is name error.')

except ValueError:
    print("The age %a is not valid"%age)

print('This is demo for raise keyword')

