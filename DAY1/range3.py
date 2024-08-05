for i in range(1, 4):
	print(i)
else: # Executed because no break in for
    print("Else block")
    print("No Break\n")
print("for loop completed")

for i in range(1, 4):
	print(i)
	break
else: # Not executed as there is a break
	print("No Break")

print("for loop completed")
