
set1 = {'one','four','three','nine',26}
set2 = {'five','one','three','four','six'}

print("Set1 :",set1)
print("Set2 :",set2)
print("------------------"*4)
print("Union of set1 and set2: ")
print("Union: ",set1|set2)
print("union : ",set1.union(set2))
print("------------------"*4)

print("Intersection of set1 and set2:")
print('Intersection :',set1&set2)
print('Intersection :',set1.intersection(set2))
print("------------------"*4)

print("Difference of set1 and set2:")
print('difference set1-set2: ',set1-set2)
print('difference set2-set1: ',set2.difference(set1))
print("------------------"*4)

print("Symmetric difference of set1 and set2:")
print('Symmetric_difference set1-set2: ',set1^set2)
print('Symmetric_difference set2-set1: ',set2.symmetric_difference(set1))
