# Finding all occurrences of a pattern

# A Python program to demonstrate working of
# findall()
import re

string = '''Hi all this is Anand rathi my reg id is
			7656465785 you can connect me at 8765769869'''

# A sample regular expression to find digits.
regex = '\d+'

match = re.findall(regex, string)
print(match)

