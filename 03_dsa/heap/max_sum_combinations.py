from heapq import heappush, heappop

def solve(nums1, nums2, k):
    minHeap = []
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            sum = nums1[i] + nums2[j]
            heappush(minHeap, sum)
            if len(minHeap) > k:
                heappop(minHeap)
    
    res = [0] * k
    for i in range(k - 1, -1, -1):
        res[i] = heappop(minHeap)
        
    return res

a1 = [3, 2]
b1 = [1, 4]
c1 = 2

a2 = [1, 4, 2, 3]
b2 = [2, 5, 1, 6]
c2 = 4
print(solve(a1, b1, c1))    # [7, 6]
print(solve(a2, b2, c2))    # [10, 9, 9, 8]