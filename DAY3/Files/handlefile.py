print('This is files demo')
# to handle any data or resource we need a variable
#
with open('first.txt','r') as file1:
    if file1:
        print('file opened')
        data = file1.readline()
        print('The cursor is at',file1.tell())
        file1.seek(40)
        print('The cursor is at',file1.tell())
    else:
        print('Please check the file name')
print('Code completed...')
