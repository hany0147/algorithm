import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def _union(a, b):
    a = _find(a)
    b = _find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def _find(x):
    if parent[x] != x:
        parent[x] = _find(parent[x])
    return parent[x]

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
for _ in range(m):
    cmd, a, b = map(int, input().split())
    if cmd == 0:
        _union(a, b)
    else:
        if _find(a) == _find(b):
            print('YES')
        else:
            print('NO')