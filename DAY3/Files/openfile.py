# open the file.txt in read mode. causes error if no such file exists.
print("Demo for Read operation")
file1 = open("file1.txt", "r")
print("File opened....")
print("------------------"*5)
# stores all the data of the file into the variable content
print("Reading the data..:")
content = file1.read(15)

# prints the content of the file
print("The data is: \n",content)

# prints the type of the data stored in the file
print(type(content))

# closes the opened file
file1.close()
print("File closed...")
