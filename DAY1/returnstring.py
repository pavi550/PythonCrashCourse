def add_is(string):
  """Adds "Is" to the beginning of a string if it doesn't already start with "Is".

  Args:
    string: The input string.

  Returns:
    The modified string with "Is" added at the beginning, or the original string if it already starts with "Is".
  """

  if string.startswith("Is"):
    return string
  else:
    return "Is" + string

# Get input from the user
input_string = input("Enter a string: ")

# Call the function and print the result
result = add_is(input_string)
print(result)
