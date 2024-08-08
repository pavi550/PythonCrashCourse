import re

# \d is equivalent to [0-9].
p = re.compile('\d')
print(p.findall("This is December 2021, we will welcome 2022 soon"))

# \d+ will match a group on [0-9], group
# of one or greater size
p = re.compile('\d+')
print(p.findall("This is December 2021, we will welcome 2022 soon"))

p = re.compile('\d*')
print(p.findall("This is December 2021, we will welcome 2022 soon"))

