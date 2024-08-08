#os.close()
#This function closes the associated file with descriptor fr.

import os
fr = "Python.txt"
file = open(fr, 'r')
text = file.read()
print(text)
file.close()