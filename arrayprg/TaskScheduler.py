import heapq

tasks = ["A","A","A","B","B","B"]

from collections import Counter, deque
count = Counter(tasks)
print(count)
max_heap = [-item for item in count.values()]
heapq.heapify(max_heap)
q = deque()
time = 0
n = 2
while max_heap or q:
    time += 1
    if max_heap:
        cnt = 1 + heapq.heappop(max_heap)
        if cnt:
            q.append([cnt, time+n])
    if q and q[0][1] == time:
        heapq.heappush(max_heap, q.popleft()[0])
print(time)

condition = True
if condition: 5 else: 7