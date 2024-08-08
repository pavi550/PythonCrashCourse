try :
    #files = open('file1.txt','r')

    with open("file1.txt", 'r') as file:
        print("Opening File in Read mode")
        for line in file:
            words = line.split()
            capitalized_words = [word.capitalize() for word in words]
            print(' '.join(capitalized_words))


except (ZeroDivisionError, TypeError, NameError) as e:
    print("it has error")
else:
    print("Please open the file in read mode")
    print("File read operation completed")

    #files.close()
    print('File closed !')