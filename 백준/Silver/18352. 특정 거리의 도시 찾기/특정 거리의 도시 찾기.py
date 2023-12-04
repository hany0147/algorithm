import sys
from collections import deque

input = sys.stdin.readline

n, m, k, x = map(int, input().split())
lst = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    lst[a].append(b)

q = deque()
q.append([x, 0])
visited = [0] * (n + 1)
visited[x] = 1
flag = False
result = []
while q:
    node, dist = q.popleft()

    if dist == k:
        result.append(node)
        flag = True

    for nxt_node in lst[node]:
        if not visited[nxt_node]:
            visited[nxt_node] = 1
            q.append([nxt_node, dist + 1])

result.sort()
if not flag:
    print(-1)
else:
    for i in result:
        print(i)