#input string
text = input("Enter a string: ")

#print output with rules
print("Output: ", " ".join(w.capitalize() for w in text.split()))
