import sys
input = sys.stdin.readline
n, m = map(int, input().split())
lst_a = []
lst_b = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    lst_a.append(tmp)
for _ in range(n):
    tmp = list(map(int, input().split()))
    lst_b.append(tmp)

lst = [[0] * m for _ in range(n)]
for x in range(n):
    for y in range(m):
        lst[x][y] = lst_a[x][y] + lst_b[x][y]

for i in lst:
    print(*i)