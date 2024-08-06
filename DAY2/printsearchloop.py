# Printing and Searching for the element in the
#list using for loop

list3 = [1,2,3,"Pune","Mumbai",764,332,22,"Delhi"]
for element in list3:
    print(element)

if "Pune" in list3:          # Membership operator
    print("The element exists in your list")
else:
    print("element does not match")
