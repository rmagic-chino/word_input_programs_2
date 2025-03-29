#input string
text = input("Enter a string: ")
width = int(input("Enter the width: "))
#input width

#print output
print("Output: ", text + " " * max(0, width - len(text)))
