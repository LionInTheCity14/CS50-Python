from math import inf
def max_subarray_sum(nums, k):
    l, sum = 0, 0
    mx = -inf
    
    for r in range(len(nums)):
        sum += nums[r]
        if r - l + 1 == k:
            mx = max(mx, sum)
            sum -= nums[l]
            l += 1

    return mx

nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
nums2 = [5, 0, 1, 4, 3, 2]

print(max_subarray_sum(nums1, 3))
print(max_subarray_sum(nums2, 3))
