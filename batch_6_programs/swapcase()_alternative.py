#input
text = input("Enter a string: ")

#print output
print("Output: ", "".join(c.lower() if c.isupper() else c.upper() for c in text))