from collections import deque
def get_maximum_in_every_subarray(nums, k):
    queue = deque()
    l, res = 0, []
    for r in range(len(nums)):
        while queue and queue[-1] < nums[r]:
            queue.pop()
        queue.append(nums[r])
        if r - l + 1 == k:
            val = queue.popleft() if nums[l] == queue[0] else queue[0]
            res.append(val)
            l += 1
    return res


nums = [1, -1, 2, 3, 5, -4, -4, -4, 10]
print(get_maximum_in_every_subarray(nums, 3))