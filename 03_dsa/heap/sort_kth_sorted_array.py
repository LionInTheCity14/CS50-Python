# aka nearly sorted array
import heapq
nums = [6, 5, 3, 2, 8, 10, 9]
k = 3

def sort_kth_sorted(nums, k):
    n, idx = len(nums), 0
    minHeap = []
    for n in nums:
        heapq.heappush(minHeap, n)
        if len(minHeap) > k:
            nums[idx] = heapq.heappop(minHeap)
            idx += 1
    
    while minHeap:
        nums[idx] = heapq.heappop(minHeap)
        idx += 1

    return nums


print(sort_kth_sorted(nums, k))