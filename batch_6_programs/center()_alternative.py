#input string
text = input("Enter a string: ")
width = int(input("Enter the width: "))
#input width

#print output
print("Output: ", text.rjust((width + len(text)) // 2).ljust(width))
 