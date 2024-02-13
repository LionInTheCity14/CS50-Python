cmnums1 = [1,2,3,4,5,6]
pattern1 = [1,1]
nums2 = [1,4,4,1,3,5,5,3]
pattern2 = [1,0,-1]

"""
nums[i + k + 1] > nums[i + k] if pattern[k] == 1.
nums[i + k + 1] == nums[i + k] if pattern[k] == 0.
nums[i + k + 1] < nums[i + k] if pattern[k] == -1.
"""
def find_pattern_cnt(nums, pattern):
    n, m = len(nums), len(pattern)
    pattern_size = len(pattern) + 1
    cnt = 0
    for j in range(n - m + 1):
        i = j
        for k in range(len(pattern)):
            if pattern[k] == 1 and nums[i + k + 1] > nums[i + k]:
                cnt += 1
            elif pattern[k] == 0 and nums[i + k + 1] == nums[i + k]:
                cnt += 1
            elif pattern[k] == -1 and nums[i + k + 1] == nums[i + k]:
                cnt += 1
            i += 1
    return cnt

print(find_pattern_cnt(nums1, pattern1))    # 4
print(find_pattern_cnt(nums2, pattern2))    # 2