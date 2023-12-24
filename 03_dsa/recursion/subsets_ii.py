def subset_II(nums):
    result = []
    def helper(idx, subset):
        if idx == len(nums):
            result.append(subset[::])
            return
        # select
        subset.append(nums[idx])
        helper(idx + 1, subset)
        subset.pop()
        
        # all the subsets which doesn't contains nums[idx]
        while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
            idx += 1
        helper(idx + 1, subset)

    helper(0, [])
    result.sort()
    return result

nums = [1, 2, 2]
print(f"subset with duplicates are :", subset_II(nums))