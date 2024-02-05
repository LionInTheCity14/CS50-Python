import math
def maximumSubarraySum(nums, k) -> int:
    def findSum(i, j):
        sum = 0
        for k in range(i, j + 1):
            sum += nums[k]
        return sum
    
    maxSum = float('-inf')
    for i in range(len(nums) - 1):
        low, high = nums[i] - k, nums[i] + k
        for j in range(i + 1, len(nums)):
            if nums[j] == low or nums[j] == high:
                sum = findSum(i, j)
                maxSum = max(maxSum, sum)

    return maxSum

print(maximumSubarraySum([1,2,3,4,5,6], 1)) # 11
print(maximumSubarraySum([-1,3,2,4,5], 3))  # 11
print(maximumSubarraySum([-1,-2,-3,-4], 2)) # -6