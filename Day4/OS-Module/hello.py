import os
#Creating a file
file1 = os.popen("Hello.txt", 'w')

#A file named Hello.txt is created in the
#current working directory.

#Adding content to the created file
file1 = os.popen("Hello.txt", 'w')
print("File opened..")
file1.write("Hello there! This is a Python demo for os module")
print("Data written to the file")
print("Closing the file")
os.close(1)
