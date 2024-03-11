def find_largest_area_histogram(nums):
    res = []
    nsl, nsr = find_next_smaller_left(nums), find_next_smaller_right(nums)
    for i in range(len(nums)):
        mx_length = nsr[i] - nsl[i] - 1     # n - (-1) -1
        area = nums[i] * mx_length
        res.append(area)
    return res

def find_next_smaller_left(nums):
    stack, res = [], []
    for i in range(len(nums)):
        if not stack:   res.append(-1)
        elif stack[-1][0] < nums[i]:   res.append(stack[-1][1])
        else:
            while stack and stack[-1][0] >= nums[i]:    stack.pop()
            if not stack:   res.append(-1)
            else:   res.append(stack[-1][1])
        stack.append([nums[i], i])
    return res

def find_next_smaller_right(nums):
    stack, res, n = [], [], len(nums)
    for i in range(n - 1, -1, -1):
        if not stack:   res.append(n)
        elif stack[-1][0] < nums[i]:    res.append(stack[-1][1])
        else:
            while stack and stack[-1][0] >= nums[i]:    stack.pop()
            if not stack:   res.append(n)
            else:   res.append(stack[-1][1])
        stack.append([nums[i], i])
    res.reverse()
    return res 

nums = [6, 2, 5, 4, 5, 1, 6]
print(find_largest_area_histogram(nums))