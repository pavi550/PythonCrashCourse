student=["Virat",20,"Pune","Computers",87]
student.append(10)
print("New list : ",student)

student.insert(3,30)
print("lis is:  ",student)

student.__delitem__(3)

print("list is:  ",student)
a=student.pop()

print("list is:  ",a)

student.clear()
print("list is:  ",student)

str1 = 'Programming'
list1 = list(str1)
print(str1)

print(list1[3:5])

list1.reverse()

print(list1)