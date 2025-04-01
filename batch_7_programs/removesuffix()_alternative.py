#input string
user_input = input("Enter a string: ")
suffix = input("Enter a suffix to remove: ")
#input suffix to remove

#set conditions
if user_input.endswith(suffix):
    user_input = user_input[:len(user_input) - len(suffix)]

#print output
print("Trimmed string:", user_input)
