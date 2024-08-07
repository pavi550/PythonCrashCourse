#Removing the element using del
print('Removing elements using del()')
list1 = [1,2,34,5,6,7,8,9]  # list of numbers
print("The List we have is:\n ",list1)
print("element at index: ",list1[1:3])
del list1[1:3]  # 1,2
print("Modified list is:\n",list1)

print("*************"*3)
list2 = ["Nashik","Khalapur","Pune","Mumbai"]
print("The List we have is: \n",list2)
print("element at index:\n ",list2[0])
del list2[0]
print("Modified list is:\n",list2)
print("*************"*3)
print("The List we have is:\n ",list1)
print("Deleting the entire list")
del list1
print("List deleted...")
#print("The List we have is:\n ",list1)
