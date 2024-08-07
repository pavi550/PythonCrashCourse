import re

str=" I am alphabate of the emotional each no , it has the common sense of the letter oval. A E I O U are oval's "
pattern = r","

split_result = str.split(' ')
print("Split result:\n", split_result)

countofo=str.count('o')

print("Total count of O :", countofo)

strremove=str.replace("each", "")

print("remove a char: ", strremove)

str1=input("ENTER a String :")

str2=str1[::-1]
print(str2)
if (str1==str2) :
    print("Its a pandrome")

else :
    print("its not palandrome")


match=str.lower().find('the')

print("match :",match)

letters=len(str)

print("count : ",letters )
