nums = [7, 10, 4, 3, 20, 15]
k = 3
import heapq
def find_kth_smallest(nums, k):
    n = len(nums)
    k %= n
    maxHeap = []
    for n in nums:
        heapq.heappush(maxHeap, n * -1)
        if len(maxHeap) > k:
            heapq.heappop(maxHeap)
    return maxHeap[0] * -1

print(find_kth_smallest(nums, k))