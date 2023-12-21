# Queue (double ended queue)
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)    # deque([1, 2, 3])

queue.pop()
queue.popleft()
print(queue)    # deque([2])

queue.appendleft(7)
queue.appendleft(8)
print(queue)    # deque([8, 7, 2])
