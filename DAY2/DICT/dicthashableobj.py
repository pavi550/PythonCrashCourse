set1 = frozenset({3,2,5})  # hashable object
print("The set is:\n",set1)
print(type(set1))
print("---------------"*5)


d1 = {set1:'frozenset',2:'Python'}
print("The dictionary is:\n",d1)
print(type(d1))
print("---------------"*5)

list1 = [1,2,3]   # unhashable object
print("The list is: ",list1)
print("---------------"*5)

# d1 = {list1:'List',2:'Python'}
# print("The dictionary is:\n",d1)
# print(type(d1))

