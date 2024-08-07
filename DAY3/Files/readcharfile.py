
try :
    file2=open("file1.txt",'r')
    content=file2.read()
    print("No of characters in a file : ",len(content))

except (ZeroDivisionError, TypeError, NameError) as e:
    print("it has error")

else:
    print("This is the else block")
    file2.close()
    print('File closed !')