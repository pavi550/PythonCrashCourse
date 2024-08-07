def print_odd_index_odd_numbers(numbers):
  """Prints odd numbers at odd indices from a list.

  Args:
    numbers: The input list of numbers.
  """

  for i in range(1, len(numbers), 2):
    if numbers[i] % 2 != 0:
      print(numbers[i])

# Example usage:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print_odd_index_odd_numbers(numbers)

