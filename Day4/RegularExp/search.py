import re

s = 'Python is a general purpose programming language'

match = re.search(r'purpose', s)

print('Start Index:', match.start())
print('End Index:', match.end())
