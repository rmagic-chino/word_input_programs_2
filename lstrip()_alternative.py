#input
text = input("Enter a string: ")

#enter rules
while text and text[0] == ' ':
    text = text[1:]

#print output
print("Output: ", text)
