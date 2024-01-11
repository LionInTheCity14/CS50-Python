"""
arr = [1, 2 ,3]
print(arr)

# can be used as a stack
arr.append(4)   # O(1)
arr.append(5)
print(arr)

arr.pop()       # O(1)
print(arr)

# technically this is array so we can insert in middle
arr.insert(1, 7)    # O(n)
print(arr)

# reassign the value    O(1)
arr[3] = 0   # O(1)
print(arr)

# initialize arr of size n with default value of 1

n = 5
arr = [1] * n
print(len(arr), arr)    # 5, [1, 1, 1, 1, 1]

arr = [1, 2, 3, 4, 5]
# CAREFUL:  -1 is not out of bounds, its the last value
print(arr[-1], arr[-2]) # 5, 4

# sublists aka slicing (last idx is non-inclusive)
print(arr[1:3], arr) # [2, 3], [1, 2, 3, 4, 5]
print(arr[0 : len(arr)], arr)

# unpacking 
a, b, c = [1, 2, 3]
# print(a, b, c)

"""

# loop through arrays
nums = [1, 2, 3, 4]

# using index

for idx in range(len(nums)):
    print(nums[idx])

for num in nums:
    print(num) 

for idx, num in enumerate(nums):
    print(idx, num)

# loop through multiple arrays simultaneously
# with unpacking
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]
for n1, n2 in zip(nums1, nums2):
    print(n1, n2)

# to reverse an array
def reverse(nums) -> int:
    i, j = 0, len(nums) - 1
    while(i < j):
        swap(nums, i, j)
        i += 1
        j -= 1
    return nums

def swap(nums,i,j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp

print(reverse(nums))

# or
nums.reverse()
print(nums)

# sort
arr = [5, 4, 7, 3, 8]
arr.sort()  # assending order
print(arr)

arr.sort(reverse=True)  # dessending order
print(arr)

# sorting list of string
arr = ["bob", "alice", "jane", "doe"]
# arr.sort()
print("array of string", arr)

# custom sort (by length of string)
arr.sort(key=lambda x : len(x))
print(arr)

# list comprehension
arr = [i for i in range(10)]
print("new array", arr)
# 2d list
# arr2d = [[0] * 4 for i in range(4)]
arr2d = [[i for i in range (4)] for j in range(2)]
print("2d array", arr2d)