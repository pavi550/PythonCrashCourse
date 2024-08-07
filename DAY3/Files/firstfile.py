files = open('first.txt','r')

print("Opening File in Read mode")

if files:
    data=files.readlines()
    print(data)
else:
    print("Please open the file in read mode")
print("File read operation completed")

files.close()
print('File closed !')
