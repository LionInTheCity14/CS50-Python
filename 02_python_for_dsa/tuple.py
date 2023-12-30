# tuples are like arrays but immutable
tup = (1, 2, 3)
print(tup)
print(tup[0])

# can't modify
# tup[0] = 9

# can be used as key for hash map/set because 
# lists can't be keys

myMap = {(1, 2): 3}
print(myMap)

mySet = set()
mySet.add((1, 2))
print((1, 2) in mySet)

 