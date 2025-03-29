#input string
text = input("Enter a string: ")
suffix = input("Enter a suffix to check: ")
#input

#print output
print("Output: ", text[-len(suffix):] == suffix)
