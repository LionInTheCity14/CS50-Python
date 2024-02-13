from collections import deque

def first_neg(nums, k):
    queue = deque()
    l, res = 0, []
    for r in range(len(nums)):
        if nums[r] < 0:
            queue.append(nums[r])
        
        if r - l + 1 == k:
            val = 0
            if queue:
                val = queue.popleft() if nums[l] < 0 else queue[0]
            res.append(val)
            l += 1
    
    return res

nums = [12, -1, -7, 8, -15, 30, 16, 28]
# queue = [-1, -7, -15]
print(first_neg(nums, 3))
# [-1, -1, -7, -15, -15, 0]