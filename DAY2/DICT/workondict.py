print("creating a empty set:")
d2 = set()
print(d2)
print(type(d2))
print("-----------------"*5)

print("Creating empty dictionary:")
d2 ={}   # empty dict
print("The empty dictionary is:",d2)
print("-----------------"*5)

print("Adding elements to the dictionary:")
d2[0]=101
d2[1]=102
print("The dictionary is:\n",d2)
print("-----------------"*5)

print("Accessing dict elements using get().")
a = d2.get(1)
print("d2.get(1) :",a)
print("d2.get(0) :",d2.get(3))
#print("d2.get(0) :",d2[3])
print("-----------------"*5)
