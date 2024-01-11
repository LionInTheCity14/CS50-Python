# from collections import List

def search(nums, target) -> int:
    l, r = 0, len(nums) - 1
    while l < r:
        mid = l + (r - l) // 2
        if nums[mid] >= target:
            r = mid
        else:
            l = mid + 1
        
    if nums[l] == target:
        return l
    else:
        return -1
    
nums = [1, 2, 3, 4, 5, 9, 10, 12]
print(search(nums, 9))

# def maxmin(arr) -> int:
#     def condition(val) -> bool:
#         pass
#     l, r = 0, len(arr) - 1
#     while l < r:
#         if condition(mid):
#             r = mid
#         else:
#             l = mid + 1
#     return l