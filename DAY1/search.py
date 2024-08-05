import re

text="I am a good boy"

pattern=r"boy"
search=re.search(pattern,text)

if search :
    print("found")

else :
    print("NA")

