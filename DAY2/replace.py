#Syntax: replace(old, new[, count])

str = "Python is a programming language"  
  
str2 = str.replace("Python","Java")  
print(str)  
print(str2) 
str2 = str.replace("g","$$",3)
print(str2)

str2 = str.replace(str,"Welcome to the Python")
print(str2)
