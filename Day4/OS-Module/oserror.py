import os  
  
try:  
    # If file does not exist,  
    # then it throw an IOError  
    filename = 'Python.txt'  
    f = open(filename, 'r')  
    text = f.read()  
    f.close()  
  
# The Control jumps directly to here if  
# any lines throws IOError.  
except IOError:  
  
    # print(os.error) will <class 'OSError'>  
    print('Problem reading: ' + filename)
