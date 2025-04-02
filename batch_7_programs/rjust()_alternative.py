#input string
user_input = input("Enter a string: ")
total_length = int(input("Enter the total length: "))

#set conditions
padded_str = ' ' * (total_length - len(user_input)) + user_input

#print output
print("padded string: ", padded_str)
