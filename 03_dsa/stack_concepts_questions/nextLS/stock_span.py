def find_max_span(nums):
    stack, res = [], []
    for i in range(len(nums)):
        if not stack:   res.append(1)
        elif stack[-1][0] > nums[i]:   res.append(i - stack[-1][1])
        else:
            while stack and stack[-1][0] <= nums[i]:   stack.pop()
            if not stack:   res.append(1)
            elif stack[-1][0] > nums[i]:   res.append(i - stack[-1][1])
        stack.append([nums[i], i])
    
    return res

nums = [100, 80, 60, 70, 60, 75, 85]
print(find_max_span(nums))