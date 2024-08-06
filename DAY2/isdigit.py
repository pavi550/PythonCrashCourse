
str = '98765'  

str2 = str.isdigit()  
 
print(str2)  

str = '980-123-8765'
print(str.isdigit())

#----------------------

str = "!@#12234t*&^%"  
if str.isdigit() == True:  
    print("The Given String is digit")  
else:  
    print("The Given String is not a digit") 
