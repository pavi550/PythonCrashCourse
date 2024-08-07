file1 = open("file2.txt", "r")
print("Reading the data using number of characters")
content = file1.read(25)
print(content)
print("+++++++++++++++++++++++++++++++++")


print("Reading the data line by line")
content = file1.readline()
print(content)
print("+++++++++++++++++++++++++++++++++")
print("Reading the data completely")
content = file1.read()
print(content)

file1.close()
print("File closed!")

# closing the opened file
file1.close()
print("file closed")
