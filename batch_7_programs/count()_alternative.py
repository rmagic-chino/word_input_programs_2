#input string
user_input = input("Enter a string: ")
substring = input("Enter a substring to check: ")
#input substring to check

#set rules and conditions
count, index = 0, 0
while (index := user_input.find(substring, index)) != -1:
    count += 1
    index += len(substring)

#print output
print("Count of substring:", count)
