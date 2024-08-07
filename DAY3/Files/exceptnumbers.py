try :
    files = open('file1.txt','r')
    print("Opening File in Read mode")
    content=files.read()
    for line in content :
        for word in line.split() :
            if not word.isdigit() :
                print(word)

except (ZeroDivisionError, TypeError, NameError) as e:
    print("it has error")
else:
    print("Please open the file in read mode")
    print("File read operation completed")

    files.close()
    print('File closed !')