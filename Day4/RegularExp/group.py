import re
xx = "python3 is more developed version"
print("The string is: ",xx)

match1 = re.match(r'(.*) is (.*)',xx)
print(match1.group(1))
print(match1.group(2)
