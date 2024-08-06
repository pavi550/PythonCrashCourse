dict1 = {1:10,2:20,3:30}  # key : value
print("The Dict is :\n",dict1)
print(type(dict1))
print("--------------------"*5)

print("Removing element using pop() ")
print("dict1.pop(1) :",dict1.pop(1))    # returns the value in the o/p and deletes the element
print("The  updated dict is:\n",dict1)
print("--------------------"*5)

dict1[1.5] = 45
dict1[7] = 90
print("The  updated dict is:\n",dict1)
print("--------------------"*5)

print("Removing element using popitem()")
print("dict1.popitem() :",dict1.popitem())  # returns the key:value pair in the o/p
print("The  updated dict is:\n",dict1)

