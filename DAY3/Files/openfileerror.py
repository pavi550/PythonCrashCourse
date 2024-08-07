# open the file.txt in read mode. causes error if no such file exists.
print("Demo For reading the file")
file1 = open("file1.txt", "r")
print("File opened")
# stores all the data of the file into the variable content
print("Reading the file")
content = file1.read(10)   # reading 10 characters from the file
# prints the type of the data stored in the file
print(type(content))
print("The data in the file is: \n")
# prints the content of the file
print(content)
print(len(content))
print("*******************"*2)
print("Reading the file")
content = file1.read(20)   # reading next 20 characters from the file
# prints the type of the data stored in the file
print(type(content))
print("The data in the file is: \n")
# prints the content of the file
print(content)
print(len(content))
print("*******************"*2)
print("Reading the file")
content = file1.read()   # reading complete data
# prints the type of the data stored in the file
print(type(content))
print("The data in the file is: \n")
# prints the content of the file
print(content)
print(len(content))

# closes the opened file
file1.close()
print("Closing the file")
print("Code ended....")
