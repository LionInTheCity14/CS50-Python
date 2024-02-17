import heapq
nums = [7, 10, 4, 3, 20, 15]
k = 3

def find_kth_largest(nums, k):
    n = len(nums)
    k %= n
    minHeap = []
    for n in nums:
        heapq.heappush(minHeap, n)
        if len(minHeap) > k:
            heapq.heappop(minHeap)
    return minHeap[0]

print(find_kth_largest(nums, k))