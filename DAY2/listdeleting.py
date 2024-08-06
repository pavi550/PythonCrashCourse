# Deleting the element
list1 = [1,2,34,5,6,7,8,9]  # list of numbers
print("The List we have is: ",list1)
#
print("Length ",len(list1))
print('list1[2:5]: ',list1[2:5])
del list1[2:5]  # del takes the index
print("Modified list is: ",list1)
print("Length ",len(list1))
print("***********"*4)
print("Modified list is: ",list1)
print("removing element using pop()")
list1.pop()   # removes the last element
print("Modified list is: ",list1)
print("***********"*4)
print("removing element using pop(index)")
list1.pop(2)   # removes the element at index
print("Modified list is: ",list1)
print("***********"*4)
list1.append([2,13,43,55])
print("Modified list is: ",list1)
print(list1[3])
list1[3].pop(2)
print("Modified list is: ",list1)
print("***********"*4)
print("Clearing the list elements")
list1.clear()   # used to clear the list
print("Modified list is: ",list1)
