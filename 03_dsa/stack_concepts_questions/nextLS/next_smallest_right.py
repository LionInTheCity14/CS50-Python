def find_next_smallest_right(nums):
    stack, res = [], []
    n = len(nums)
    for i in range(n - 1, -1, -1):
        if not stack:   res.append(-1)
        elif stack[-1] < nums[i]:   res.append(stack[-1])
        else:
            while stack and stack[-1] >= nums[i]:   stack.pop()
            if not stack:   res.append(-1)
            elif stack[-1] < nums[i]:   res.append(stack[-1])
        stack.append(nums[i])

    i, j = 0, n - 1
    while i < j:
        res[i], res[j] = res[j], res[i]
        i, j = i + 1, j - 1
    
    return res

nums = [1, 3, 2, 1, 4, 0]
print(find_next_smallest_right(nums))