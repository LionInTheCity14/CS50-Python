def find_next_largest_left(nums):
    stack, res, n = [], [], len(nums)
    for i in range(n):
        if not stack:   res.append(-1)
        elif stack[-1] > nums[i]:   res.append(stack[-1])
        else:
            while stack and stack[-1] <= nums[i]:   stack.pop()
            if not stack:   res.append(-1)
            elif stack[-1] > nums[i]:   res.append(stack[-1])
        stack.append(nums[i])

    return res

nums = [1, 3, 0, 0, 1, 4]
print(find_next_largest_left(nums))