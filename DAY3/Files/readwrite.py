try :
    file2=open("file1.txt",'r')
    content=file2.read()
    print(content)
    file3=open("file1.txt","w")
    file3.write(content)
    file3 = open("file1.txt", "r")
    details=file3.read()
    print(details)
except (ZeroDivisionError, TypeError, NameError) as e:
    print("it has error")

else:
    print("This is the else block")
    file2.close()
    file3.close()
    print('File closed !')