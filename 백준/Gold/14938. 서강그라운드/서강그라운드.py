import sys
input = sys.stdin.readline
n, m, r = map(int, input().split())
# 수색범위(m)을 넘어서면 제외한다.
items = list(map(int, input().split()))
INF = 1e9
ground = [[INF] * n for _ in range(n)]

for a in range(n):
    for b in range(n):
        if a == b:
            ground[a][b] = 0

for _ in range(r):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    ground[a][b] = c
    ground[b][a] = c

for k in range(n):
    for a in range(n):
        for b in range(n):
            ground[a][b] = min(ground[a][b], ground[a][k] + ground[k][b])
# print(ground)
lst = []
for a in range(n):
    res = 0
    for b in range(n):
        if ground[a][b] <= m:
            res += items[b]
    lst.append(res)
# print(lst)
print(max(lst))
