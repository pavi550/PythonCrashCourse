def create_nested_tuple(num_tuples, tuple_length):
  """Creates a nested tuple with specified dimensions.

  Args:
    num_tuples: The number of tuples in the outer tuple.
    tuple_length: The length of each inner tuple.

  Returns:
    A nested tuple with the specified dimensions.
  """

  nested_tuple = ()
  for _ in range(num_tuples):
    inner_tuple = tuple(range(tuple_length))
    nested_tuple += (inner_tuple,)

  return nested_tuple

# Example usage:
num_tuples = 3
tuple_length = 4
result = create_nested_tuple(num_tuples, tuple_length)
print(result)
