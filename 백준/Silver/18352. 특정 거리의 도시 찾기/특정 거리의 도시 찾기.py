from collections import defaultdict, deque
import sys
input= sys.stdin.readline

dict_ = defaultdict(list)

n, m, k, x = map(int, input().split())
for _ in range(m):
    a, b = map(int, input().split())
    dict_[a].append(b)

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
        continue
    for nxt_node in dict_[node]:
        if not visited[nxt_node]:
            visited[nxt_node] = 1
            alt = dist + 1
            q.append([nxt_node, alt])
result.sort()
if not flag:
    print(-1)
else:
    for i in result:
        print(i)