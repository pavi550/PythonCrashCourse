print('This is files demo')

# to handle any data or resource we need a variable
file1 = open('first.txt','r')
if file1:
    print('File opened')
    data = file1.readline()         # returns single line
    print(data)
    data = file1.readline(15)
    print(data)
    print('*******'*7)
    data = file1.readlines()        # returns list of lines in file
    print(data)
    data = file1.readline()  # returns single line
    print(data)
else:
    print('Please check the file name')
file1.close()
print('This file is closed')
