# Passing  string
def update_string(string1):
    print("String inside the function:\n",string1)
    string1 = string1 + "Python is cool"
    print("\nprinting the updated string inside function :\n", string1)


string1 = "Python is a developer friendly."
print("Original string:\n",string1)
# calling the function
print("Calling the function...")
update_string(string1)

print("\nprinting the string outside function :\n", string1)
