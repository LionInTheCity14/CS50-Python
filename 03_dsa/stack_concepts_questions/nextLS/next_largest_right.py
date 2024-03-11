def find_next_largest_right(nums):
    stack = []
    res = []
    for i in range(len(nums) - 1, -1, -1):
        if not stack:
            res.append(-1)
        elif stack[-1] > nums[i]:
            res.append(stack[-1])
        else:
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            if not stack:
                res.append(-1)
            elif stack[-1] > nums[i]:
                res.append(stack[-1])
        stack.append(nums[i])

    i, j = 0, len(res) - 1
    while i < j:
        res[i], res[j] = res[j], res[i]
        i += 1
        j -= 1

    return res


nums = [1, 3, 0, 0, 1, 4]
print(find_next_largest_right(nums))