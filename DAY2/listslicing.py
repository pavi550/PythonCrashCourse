#Slicing the List

str1 = 'Programming'

list1 = list(str1)
print(list1)

print(list1[2:6])  # 2 to 5 index

print(list1[5:])   # from 5 to last

print(list1[-3:]) # last 3 elements

print(list1[::2])   # alternate elements

print(list1[::-1])  # reverse

list1.reverse()   # when reverse is applied the method returns None
print(list1)

