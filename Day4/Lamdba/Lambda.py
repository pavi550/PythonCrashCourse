# Lambda

print("Demo for the Lambda functions...")

numbers = (1,2,3,4,5)
print("The tuple is: ",numbers)

print("Using Lambda function")

result = map(lambda x: x+x , numbers)

print("The result is: ",list(result))
