# Try and Finally

try:
    fileptr = open("file1.txt","r")
    print('The file is opened...')
    try:
        print('Trying to write the data in file')
        fileptr.write("Hi I am good")
    finally:
        print('In the inner finally block')
        fileptr.close()
        print("file closed")
except:
    print('In the except block')
    print("Error- trying to write in file , opened for read operation")
finally:
     print("Final Finally block")
print('The program ended here')
