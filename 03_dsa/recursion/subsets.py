# from typing import List

def subsets(nums ):
    def solve(nums, idx , ds , result):
        if idx == len(nums):
            result.append(ds)
            return
        # select
        ds.append(nums[idx])
        solve(nums, idx + 1, ds, result)
        ds.pop()

        # not select
        solve(nums, idx + 1, ds, result)
    
    result = [[]]
    solve(nums, 0, [], result)
    return result

nums = [1, 2, 3]
print(f"subsets of {nums} are : ", subsets(nums))