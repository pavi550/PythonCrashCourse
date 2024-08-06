list1 = [1,2,34,5,6,7,8,9]  # list of numbers
print("The List we have is: ",list1)
# add multiple elements
print("Length ",len(list1))
print('list1[2:5]: ',list1[2:5])
list1[2:5]=[12,34,30,20,25,15,25]  # reassigning  list1[2] = 5
print("Modified list is: ",list1)
print("Length ",len(list1))
print("***********"*4)
list1[:] = [1,2,3,4]   # recreating the list list1 = [1,2,3,4]
print("Modified list is: ",list1)
print("***********"*4)
print("Adding multiple elements at once using extend()")
list1.extend([3,4,5,6])
print("Modified list is: ",list1)
print("***********"*4)
print("Adding list within a list")
list1.append([3,4,5,6])
print("Modified list is: ",list1)
print("***********"*4)
list1.append(40)
print("Modified list is: ",list1)
