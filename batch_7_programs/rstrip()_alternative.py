#input string
user_input = input("Enter a string: ")
index = len(user_input) - 1

#set condiitons
while index >= 0 and user_input[index] == ' ':
    index -= 1

#print output
print("Trimmed string:", user_input[:index + 1])
