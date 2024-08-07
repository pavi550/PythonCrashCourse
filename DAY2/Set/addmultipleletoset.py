# Adding multiple elements to the set

set1 = {1,2,3,3,99,6,44,81,2,3,1}
print("The set is: ",set1)
set1.update({77,54,65,33})
print("The modified set is: ",set1)
print("--------------------"*4)

set1.discard(3)
print("The modified set after discard(): ",set1)
print("--------------------"*4)

set1.discard(100)
print("The modified set after discard(): ",set1)
print("--------------------"*4)

set1.remove(2)
print("The modified set after remove(): ",set1)
# set1.remove(100)
# print(set1)
