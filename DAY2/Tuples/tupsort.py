#Using the sorted() function

tup4 = (29,32,43,22,1,12,30)
print("The tuple is:",tup4)
a = sorted(tup4)    # returns a list of sorted elements
print("sorted tuple:\n",a)
print(type(a))

sort1 = tuple(sorted(tup4))
print("sorted tuple:\n",sort1)
print(type(sort1))
