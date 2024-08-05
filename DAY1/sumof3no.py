#Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.

def sum_of_numbers(num1, num2, num3):
  """Calculates the sum of three numbers.

  Args:
    num1: The first number.
    num2: The second number.
    num3: The third number.

  Returns:
    The sum of the numbers, or three times the sum if all numbers are equal.
  """

  if num1 == num2 == num3:
    return 3 * (num1 + num2 + num3)
  else:
    return num1 + num2 + num3

# Get input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# Calculate and print the result
result = sum_of_numbers(num1, num2, num3)
print("The result is:", result)
