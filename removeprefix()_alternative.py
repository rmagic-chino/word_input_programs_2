#input string
text = input("Enter a string: ")
prefix = input("Enter prefix to remove: ")
#input prefix to remove

#set rules
if text.startswith(prefix):
    text = text[len(prefix):]

#print output
print("Output: ", text)
