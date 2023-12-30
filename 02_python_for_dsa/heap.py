import heapq

sampleArr = [3, 2 , 5, 0]

# by default python has min heap
# under the hood are arrays

minHeap = []
for num in sampleArr:
    heapq.heappush(minHeap, num)

# min is always at index 0
print(minHeap)
# print("minimum :", minHeap[0])

while len(minHeap):
    print("minimum : ", heapq.heappop(minHeap))

# no max heaps by default, work around is to use min heap and
# multiply by -1 when push and pop

maxHeap = []
for num in sampleArr:
    heapq.heappush(maxHeap, -1 * num)

# now max is always at index 0
print(maxHeap)

while len(maxHeap):
    print("maximum :", -1 * heapq.heappop(maxHeap))

print(sampleArr)
# heapq.heapify(sampleArr)  # converts sampleArr to minHeap
heapq._heapify_max(sampleArr) # maxHeap
print(sampleArr)
