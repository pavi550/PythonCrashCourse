
#\ – Backslash

import re

s = 'Python.Language'

# without using \
match = re.search(r'.', s)
print(match)

# using \
match = re.search(r'\.', s)
print(match)

