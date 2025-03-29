#input string
text = input("Enter a string: ")

#set rules
for i in range(26):
    text = text.replace(chr(65 + i), chr(97 + i))

#print output
print("Output: ", text)
