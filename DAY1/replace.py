import re

test="I am a good boy"
pattern = r"boy"
replace="girl"
new_text=re.sub(pattern, replace,test)


print("new text is:",new_text)
