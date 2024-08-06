dict1 = {'1':10,2:20,3:30}  # key : value
print("The Dict is :\n",dict1)
print(type(dict1))
print("--------------------"*5)

dict1[5] = 'one'
print("The Updated Dict is :\n",dict1)
print("--------------------"*5)

dict1[2.2] = 'one'
print("The Updated Dict is :\n",dict1)
print("--------------------"*5)

dict1[2.2] = 'Five'
print("The Updated Dict is :\n",dict1)
print("--------------------"*5)

print("Accessing dict elements using get()")
print("dict1[2] :",dict1[2])
print("dict1.get(3) :",dict1.get(3))
print("dict1.get(5) :",dict1.get(5))

