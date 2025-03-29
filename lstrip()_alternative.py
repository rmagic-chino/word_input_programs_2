#input
string = input("Enter a string: ")

#enter rules
while string and string[0] == ' ':
    string = string[1:]

#print output
print("Output: ", string)
