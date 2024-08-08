def extract_numbers_from_file(file_path):
  """Extracts numbers from a file and prints them.

  Args:
    file_path: The path to the file.
  """

  with open(file_path, 'r') as file:
    for line in file:
      words = line.split()
      for word in words:
        if word.isdigit():
          print(word)

# Example usage:
file_path = "file1.txt"  # Replace with the actual file path
extract_numbers_from_file(file_path)
