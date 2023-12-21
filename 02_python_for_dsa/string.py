# Strings are similar to arrays
s = 'abcd'
print(s[0:2])

# string are immutable
# s[0] = "g"    # error
# print(s) 

# so this create a new string
s += "efgh" # O(n)
print("new string s =", s)

print(str(123) + str(123))
# print(int("abc") + int("abc"))

# ASCII value of a char
print(ord("a"), ord("b")) # 97, 98

# combine a list of strings (with a string delimitor)

strings = ["abc", "def", "ghi", "klm"]
print("-----".join(strings))