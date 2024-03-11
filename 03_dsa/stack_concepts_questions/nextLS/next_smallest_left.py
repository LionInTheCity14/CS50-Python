def find_next_smallest_left(nums):
    stack, res, n = [], [], len(nums)
    for i in range(n):
        if not stack:   res.append(-1)
        elif stack[-1] < nums[i]:   res.append(stack[-1])
        else:
            while stack and stack[-1] >= nums[i]:   stack.pop()
            if not stack:   res.append(-1)
            elif stack[-1] < nums[i]:   res.append(stack[-1])
        stack.append(nums[i])

    return res

nums = [0, 3, 1, 2, 4, 3]
print(find_next_smallest_left(nums))