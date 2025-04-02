#input string
user_input = input("Enter a string: ")
total_length = int(input("Enter the total length: "))
#input length

#set conditions
padded_str = '0' * (total_length - len(user_input)) + user_input

#print output
print("Padded string: ", padded_str)
