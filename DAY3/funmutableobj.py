# Passing mutable Object (List)
print("Passing the list to the function")
# defining the function
def update_list(num):
    print("Inside the function")
    print("Id for list inside func:\n ", id(num))
    print("List inside function ",num)
    num.append(200)
    num.append(300)
    print("Id for list after update:\n ", id(num))
    print("Modified list inside function = ", num)

# defining the list
num = [100, 300, 400, 500]  #global
print("The list is: ",num)
print("Id for list:\n ",id(num))

# calling the function
print("Calling the list")
update_list(num)
print("list outside function = ", num)
print("Id for list outside func:\n ",id(num))
