def add1(n):
    return n + n

print(" Demo for the map()")
numbers = (1,2,3,4,5)
print("using a map function")
result = map(add1,numbers)

print("Result after using map function")
print(list(result))
