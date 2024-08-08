import os

print("The current working directory is:\n",os.getcwd())

#Deleting a directory
os.mkdir("/mnt/c/Praveen/DEVOPS/Python/Pythontest/Day4/OS-Module/Pythondemo")
print("Directory created....")
os.rmdir("/mnt/c/Praveen/DEVOPS/Python/Pythontest/Day4/OS-Module/Pythondemo") #
print("\nDirectory Deleted....")
#Renaming a directory

os.mkdir("/mnt/c/Praveen/DEVOPS/Python/Pythontest/Day4/OS-Module/Pythondemo")
print("\nDirectory created....")
print("Renameing a Direcrory")
os.rename("/mnt/c/Praveen/DEVOPS/Python/Pythontest/Day4/OS-Module/Pythondemo","/mnt/c/Praveen/DEVOPS/Python/Pythontest/Day4/OS-Module/Pythondemo2")


#Changing a directory
#The os module provides the chdir() function to change
#the current working directory.
print("Changing the dir")

os.chdir("/mnt/c/Praveen/DEVOPS/Python/Pythontest/Day4/OS-Module/")
print("The current working directory is:",os.getcwd())
