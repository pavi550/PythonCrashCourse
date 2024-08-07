with open('first.txt','w') as file1:
    if file1:
        print('file opened')
        print('The cursor is at',file1.tell())
        file1.write('''This is the first line.
        This is the 2nd line.
        This is the last line.''')
        print('The cursor is at',file1.tell())
        print('write operation completes')
    else:
        print('Please check the file name')
print('Code completed...')
