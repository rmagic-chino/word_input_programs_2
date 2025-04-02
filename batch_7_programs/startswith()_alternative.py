#input string
user_input = input("Enter a string: ")
prefix = input("Enter a prefix to check: ")

#set rules
matches = user_input[:len(prefix)] == prefix

#print output
print("Starts with prefix:", matches)
