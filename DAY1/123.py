def generate_string(string, n):
  """Generates a string by repeating a given string n times.

  Args:
    string: The string to be repeated.
    n: The number of times to repeat the string.

  Returns:
    The repeated string.
  """

  return string * n

if __name__ == "__main__":
  string = input("Enter the string: ")
  n = int(input("Enter the number of times to repeat: "))
  result = generate_string(string, n)
  print(result)
