#input string
user_input = input("Enter a string: ")
uppercase_str = ""

#construct loop
for char in user_input:
    if 'a' <= char <= 'z':
        uppercase_str += chr(ord(char) - 32)
    else:
        uppercase_str += char

#print output
print("Uppercase string:", uppercase_str)
