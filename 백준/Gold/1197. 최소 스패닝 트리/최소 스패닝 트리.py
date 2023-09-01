import heapq
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
tree = [[] for _ in range(v + 1)]
visited = [0 for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    tree[a].append([c, b])
    tree[b].append([c, a])

ans = 0
cnt = 0
q = [[0, 1]]

while q:
    if cnt == v:
        break
    weight, node = heapq.heappop(q)
    if visited[node] == 0:
        visited[node] = 1
        ans += weight
        cnt += 1
        for nxt in tree[node]:
            heapq.heappush(q, nxt)
    
print(ans)