from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)
res = {}

for i in range(1, n + 1):
    visited = [0 for _ in range(n + 1)]
    cnt = 0
    q = deque()
    q.append(i)
    while q:
        cur = q.popleft()
        if visited[cur] == 0:
            visited[cur] = 1
            cnt += 1
            for nxt in graph[cur]:
                q.append(nxt)
    res[i] = cnt

ans = []
tmp = max(res.values())
for key, value in res.items():
    if tmp <= value:
        ans.append(key)
print(*ans)
