from math import inf

matrix = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 0, 0]
]

def max_area_matrix(matrix):
    mx= -inf
    rows, cols = len(matrix), len(matrix[0])
    mx = max(mx, mah(matrix[0]))
    for r in range(1, rows):
        for c in range(cols):
            if matrix[r][c]:
                matrix[r][c] = matrix[r][c] + matrix[r - 1][c]
        mx = max(mx, mah(matrix[r]))
    print(matrix)
    return mx
    

def mah(nums):
    left, right = nsl(nums), nsr(nums)
    mx = -inf
    for i in range(len(nums)):
        mx = max(mx, nums[i] * (right[i] - left[i] - 1))
    return mx

def nsl(nums):
    stack, res = [], []
    for i in range(len(nums)):
        if not stack:   res.append(-1)
        elif stack[-1][0] < nums[i]:    res.append(stack[-1][1])
        else:
            while stack and stack[-1][0] >= nums[i]:    stack.pop()
            if not stack:   res.append(-1)
            else:   res.append(stack[-1][1])
        stack.append([nums[i], i])
    return res

def nsr(nums):
    stack, res, n =[], [], len(nums)
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

print(max_area_matrix(matrix))