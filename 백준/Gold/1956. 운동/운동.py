import sys
input = sys.stdin.readline

v, e = map(int, input().split())
INF = 1e9
cycle = [[INF] * (v + 1) for _ in range(v + 1)]
for a in range(v):
    for b in range(v):
        if a == b:
            cycle[a][b] = 0

for _ in range(e):
    a, b, c = map(int, input().split())
    cycle[a][b] = c
# print(cycle)

for k in range(1, v + 1):
    for a in range(1, v + 1):
        for b in range(1, v + 1):
            cycle[a][b] = min(cycle[a][b], cycle[a][k] + cycle[k][b])
# print(cycle)
lst = []
for a in range(1, v + 1):
    for b in range(1, v  + 1):
        sum_ = cycle[a][b] + cycle[b][a]
        if sum_ < INF and a != b:
            lst.append(sum_)
# print(lst)
if not lst:
    print(-1)
else:
    print(min(lst))