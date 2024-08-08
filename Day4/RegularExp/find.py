import re
xx = "python3 is more developed version"
r1 = re.findall(r"^\w+", xx)
print(r1)
print((re.split(r'\s','we need to write the code properly')))
print((re.split(r's','this is to split the words')))
