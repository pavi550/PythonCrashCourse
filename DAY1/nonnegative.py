#Write a Python program to get a string which is n (non-negative integer) copies of a given string. (except a string from user and how many times the string to print.print the string that many times.)
str =input ("Enter string to be printed : ")
n=int(input("Enter no of time it has to print : "))
if n <0 :
    print("Number is negative no:", n)
    break

def mul(n,str) :
    result= str * n
    print(result,end='')

mul(n,str)