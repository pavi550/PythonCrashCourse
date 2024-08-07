
#Read Lines of the file using a function readline() and readlines()

file1 = open("file1.txt","r")   
  
#stores all the data of the file into the variable content  
content = file1.readline()  
  
# prints the type of the data stored in the file  
print(type(content))   
  
#prints the content of the file  
print(content)   
  
#closes the opened file  
file1.close() 
