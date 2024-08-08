# Filter
'''
It gives sequence with help of a function that tests each element
in the sequence is true or not
'''
print("Demo for the filter()")

seq = [1,2,3,4,5,6,7,8,12,22,44]

print("The List is: ",seq)

print("Function to find odd or even numbers")

result = filter(lambda x : x%2 != 0,seq)

print("The odd numbers are:")
print(list(result))

result = filter(lambda x : x%2 == 0,seq)

print("The even numbers are:")
print(list(result))

