
#File pointer position using tell()

# open the file file2.txt in read mode  
file2 = open("file1.txt","r")
  
#initially the filepointer is at 0   
print("The filepointer is at byte :",file2.tell())  
  
#reading the content of the file  
content = file2.read()  
  
#after the read operation file pointer modifies. 
  
print("After reading, the filepointer is at:",file2.tell())  
