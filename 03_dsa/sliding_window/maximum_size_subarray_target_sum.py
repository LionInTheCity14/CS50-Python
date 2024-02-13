from math import inf
def get_max_size(nums, target):
    l, res = 0, -inf
    sum = 0
    for r in range(len(nums)):
        sum += nums[r]
        while l < r and sum > target:
            sum -= nums[l]
            l += 1
        if sum == target:
            res = max(res, r - l + 1)
    return res if res != -inf else -1


nums = [-1, -1, 3, -2, 6, 1, 1, 1, 2, 3]
print(get_max_size(nums, 5))