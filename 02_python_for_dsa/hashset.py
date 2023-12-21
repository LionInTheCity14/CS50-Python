# HashSet
mySet = set()

# inserting     O(1)
mySet.add(1)
mySet.add(1)
mySet.add(2)
mySet.add(3)
print(mySet)

# size or length    O(1)
print(len(mySet))

# search O(1)
print(1 in mySet)   # True
print(4 in mySet)   # False

# removal
returnVal = mySet.remove(1)     # None as return value
if 5 in mySet:
    mySet.remove(5)
print(1 in mySet, 5 in mySet)

# list to set

list = [1, 2 ,3, 3, 4, 1]
mySet1 = set(list)
print(mySet1)

# just like list comprehension, set also has set comprehension

mySet2 = {i for i in range(5)}
print(mySet2)