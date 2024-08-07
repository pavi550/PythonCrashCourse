list1 = [2,3,4,1,5,1,2,3,4,5]
print("The list is: ",list1)
print("--------------"*4)
print("converting list into set.")
set2 = set(list1)
print("The set is: ",set2)
print("--------------"*4)
print("Adding elements to the set")
set2.add(23)    # adding single elements
print("Updated set is: ",set2)
print("--------------"*4)
print("Adding multiple values to the set.")
set2.update([12,13,14])   # adding multiple elements
print("Updated set is: ",set2)
print("--------------"*4)

print("Converting a list to set")
number = set(["One","Two","Three"])
print(number)
print(type(number))
