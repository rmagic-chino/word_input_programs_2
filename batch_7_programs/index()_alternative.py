#input string
user_input = input("Enter a string: ")
substring = input("Enter a substring to find: ")
#input substring to find

#set conditions
index = -1
for i in range(len(user_input) - len(substring) + 1):
    if user_input[i:i + len(substring)] == substring:
        index = i
        break

#print output
print("First index of substring:", index)
