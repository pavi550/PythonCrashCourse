# Writing the file
print("Demo to write the data to file")
# open the file.txt in write mode. Creates a new file if no such file exists.
file1 = open("file1.txt", "w")
print("File opened...")
# writing the content to the file
file1.write("Machine learning is blooming technology. Python supports ML")
print("Data written to the file")
file1.write("\nMachine learning is blooming technology. Python supports ML")
print("Data written to the file")
file1.write("\nMachine learning is blooming technology. Python supports ML")
print("Data written to the file")
# closing the opened file
file1.close()
print("File closed...")
