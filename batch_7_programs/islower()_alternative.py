#input string
user_input = input("Enter a string: ")
all_lowercase = True

#construct loop
for char in user_input:
    if not ('a' <= char <= 'z'):
        all_lowercase = False
        break

#print output
print("All lowercase:", all_lowercase)
