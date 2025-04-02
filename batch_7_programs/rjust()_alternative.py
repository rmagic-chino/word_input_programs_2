#input string
user_input = input("Enter a string: ")
total_length = input("Enter the total length: "))
#input length

#set conditions
padded_str = ' ' * (total_length - len(user_input)) + user_input

#print output
print("padded string:", padded_str)
