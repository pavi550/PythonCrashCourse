#Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged

str=input("ENTER a String : ")

if str[::1]=="is" :
    print("String already starting with is",str)

else :

    print("Updated string : ","Is"+ str)