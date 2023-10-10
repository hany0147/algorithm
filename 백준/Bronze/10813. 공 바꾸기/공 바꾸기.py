n, m = map(int, input().split())
arr = []
for i in range(n + 1):
    arr.append(i)

for _ in range(m):
    a, b = map(int, input().split())
    tmp1 = arr[a]
    tmp2 = arr[b]
    arr[a] = tmp2
    arr[b] = tmp1
arr.pop(0)
print(*arr)