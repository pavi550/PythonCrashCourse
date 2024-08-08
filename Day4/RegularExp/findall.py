import re

# \w is equivalent to [a-zA-Z0-9_].
p = re.compile('\w')
print(p.findall("This is Python Program. (python3.10)"))

# \w+ matches to group of alphanumeric character.
p = re.compile('\w+')
print(p.findall("python support's OOp's concepts \
**Multiple inheritance** is applicable here"))

# \W matches to non alphanumeric characters.
p = re.compile('\W')
print(p.findall("This is 2021 *** Lets welcome 2022."))
