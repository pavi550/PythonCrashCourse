# Creating new file with x mode
print("Demo for Creating a file using A mode")

f1 = open("file3.txt", "a")

print("File is opened..")

if f1:
    print("File created successfully")
print("Closing the file")
f1.close()
print("File closed")
