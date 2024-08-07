#Raise the exception with message

try:  
     num = int(input("Enter a positive integer: "))  
     if(num <= 0):  
# we can pass the message in the raise statement  
         raise ValueError("That is  a negative number!")  
except ValueError as e:  
     print(e)  
