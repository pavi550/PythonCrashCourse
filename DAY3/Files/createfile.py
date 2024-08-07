# Creating new file with x mode
print("Demo for Creating a file using X mode")

f1 = open("file2.txt", "x")

print("File is opened..")

if f1:
    print("File created successfully")
print("Closing the file")
f1.close()
print("File closed")
