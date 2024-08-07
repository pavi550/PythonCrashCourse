#Iterate a Dictionary


emp = {'name':'Laxman','id':1010,'Age':34,'salary':80000}

for x in emp:     # print the keys only
    print(x)
print('****'*10)

for x in emp:     # print the values
    print(emp[x])
print('****'*10)

for x in emp.values():   # print the values
    print(x)
print('****'*10)

for x in emp.items():   # print the keys and values
    print(x)
print('****'*10)

for x,y in emp.items():   # print the keys and values
    print(x,' is the ',y)
