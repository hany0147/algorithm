n = int(input())
r = n // 5
c = n // 3

matrix = [[5001] * (c + 1) for _ in range(r + 1)]

for x in range(r + 1):
    for y in range(c + 1):
        if 5 * x + 3 * y == n:
            matrix[r][c] = min(matrix[r][c], x + y)

ans = 5001
for i in matrix:
    ans = min(ans, min(i))
if ans == 5001:
    print(-1)
else:
    print(ans)