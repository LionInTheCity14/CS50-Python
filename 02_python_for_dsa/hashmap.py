# HashMap (aka dist)
myMap = {}

# assigning a key value pair
myMap["alice"] = 88
myMap[2] = 77
myMap[True] = False
print("myMap", myMap)

# modifying a key value pair
myMap["alice"] = "ron"
myMap[2] += 45
print("after modification", myMap)


# search O(1)
print("alice" in myMap) # True
print(True in myMap)    # True
print(45 in myMap)      # False

# intialize a hashmap
myMap1 = {"alice" : 90, 7 : 70, 8 : 80}
print("new myMap1", myMap1)

# just like other comprehensions, hashmap also has one
mySet2 = {i for i in range(5)}
myMap2 = {i : i * 10 for i in range(5)}
print("set :", mySet2)
print("map :", myMap2)

# looping through a map
# for key in mySet2:
#     print(key)

# for key in myMap2:
#     print(key, myMap2[key])

# for val in myMap2.values():
#     print(val)

for key,val in myMap2.items():
    print(key, val)

print(myMap2.items())