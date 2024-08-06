day1 = {"One","Two","Three","Six","Four"}
day2 = {"Five","One","Six","Seven","Two"}
print("Day1 set: ",day1)
print("Day2 set: ",day2)
print("------------------"*4)
#Intersection of two sets
print("day1&day2 : ",day1&day2)
print("day1.intersection(day2): ",day1.intersection(day2))  # printing intersection
print("------------------"*4)
#Prints only the intersection elements

day1 = {"One","Two","Three","Six","Four"}
print("Day1 set: ",day1)
print("Day2 set: ",day2)
print("------------------"*4)
print("Set intersection using intersection_update()")
day1.intersection_update(day1,day2)
print("Updated set after intersection: ",day1)

