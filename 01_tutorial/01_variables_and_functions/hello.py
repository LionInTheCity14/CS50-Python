# Ask user for their name
name = input("What's your name? ").strip().title()

# Split user's name into first name and last name
nameArr = name.split(" ")
print(nameArr)
first = nameArr[0]
last = nameArr[-1]

# Remove whitespace from str and capitalize user's name
# name = name.strip().title()

# Capitalize user's name
# name = name.title()

# Say hello to user
# print("hello, ", end="")
# print(name)

# print("hello, " + name) 

# print("hello,", name)

# print("hello,", str(name))

# print('hello', name, sep="<<<",end=">>>")
# print()

print(f"hello, {first} {last}")
