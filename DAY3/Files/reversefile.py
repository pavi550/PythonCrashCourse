try :
    files = open('file1.txt','r')
    print("Opening File in Read mode")
    content=files.read()
    print ("Total spaces :" , content[::-1])
    print("Total no of lines : ", len(content))

except (ZeroDivisionError, TypeError, NameError) as e:
    print("it has error")
else:
    print("Please open the file in read mode")
    print("File read operation completed")

    files.close()
    print('File closed !')