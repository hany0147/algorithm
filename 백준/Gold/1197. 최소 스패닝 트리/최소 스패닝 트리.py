import sys
input = sys.stdin.readline


def _union(a, b):
    a = _find(a)
    b = _find(b)

    if a == b:
        return
    if rank[a] < rank[b]:
        parent[a] = b
    elif rank[a] > rank[b]:
        parent[b] = a
    else:
        parent[a] = b
        rank[b] += 1

def _find(x):
    while parent[x] != x:
        x = parent[x]
    return x

v, e = map(int, input().split())
link = [list(map(int, input().split())) for _ in range(e)]
link.sort(key=lambda x: x[2])

parent = [i for i in range(v + 1)]
rank = [0 for _ in range(1_000_001)]
ans = 0
for i in range(e):
    a = link[i][0]
    b = link[i][1]
    weight = link[i][2]

    if _find(a) == _find(b):
        continue
    _union(a, b)
    ans += weight

print(ans)