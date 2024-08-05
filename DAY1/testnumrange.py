#Write a Python program to test whether a number is within 100 of 1000 or 2000

def check_number_range(number):
  """Checks if a number is within 100, 1000, or 2000.

  Args:
    number: The number to check.

  Returns:
    A string indicating the range the number belongs to, or "Out of range" if not within any range.
  """

  if number <= 100:
    return "Within 100"
  elif number <= 1000:
    return "Within 1000"
  elif number <= 2000:
    return "Within 2000"
  else:
    return "Out of range"

if __name__ == "__main__":
  number = int(input("Enter a number: "))
  result = check_number_range(number)
  print(result)

