import re
text1="Python, is awesome"
print(text1.split(","))

text2 = "apple,banana,orange,grape"
pattern = r","

split_result = re.split(pattern, text2)
print("Split result:", split_result)
