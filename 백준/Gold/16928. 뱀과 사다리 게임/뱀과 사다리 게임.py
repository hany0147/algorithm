import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
graph = [ i for i in range(101) ]
for _ in range(n + m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a] = b
q = deque()
q.append(1)
visit = [0]*(101)
visit[1] = 0
while q:
    now = q.popleft()
    for i in range(1, 7):
        next = now + i
        if next > 100:
            continue
        ladder = graph[next]
        if not visit[ladder]:
            q.append(ladder)
            visit[ladder] = visit[now] + 1
            
print(visit[100])