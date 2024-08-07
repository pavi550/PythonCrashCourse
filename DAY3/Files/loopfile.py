#Looping through the file

file1 = open("file1.txt","r")

for i in file1:
	print(i) # here i contains each line of the file

file1.close()
print("code ended..")
