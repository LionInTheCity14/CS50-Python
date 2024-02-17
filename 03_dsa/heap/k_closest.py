from heapq import heappush, heappop
nums = [5, 6, 7, 8, 9]
k = 3
x = 7

def k_closest(nums, k, x):
    res = []
    maxHeap = []
    for n in nums:
        dif = abs(x - n)
        heappush(maxHeap, [ -1 * dif, n])
        
        if len(maxHeap) > k:
            heappop(maxHeap)
    
    while maxHeap:
        _, val = heappop(maxHeap)
        res.append(val)

    return res

print(k_closest(nums, k, x))