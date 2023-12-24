# from typing import List
def subsets(nums ):
    result = []
    def solve(idx , ds):
        if idx == len(nums):
            result.append(ds[::])
            return
        # select
        ds.append(nums[idx])
        solve(idx + 1, ds)
        ds.pop()

        # not select
        solve(idx + 1, ds)
    
    solve(0, [])
    result.sort()
    return result

nums = [1, 2, 2]
print(f"subsets of {nums} are : ", subsets(nums))