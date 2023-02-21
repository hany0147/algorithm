check = [[0] * 101 for _ in range(101)]
# print(check)

for _ in range(4):
    x1, y1, x2, y2 = list(map(int, input().split()))

    for x in range(x1, x2):
        for y in range(y1, y2):
            check[x][y] = 1

sum_ = 0
for x in range(101):
    sum_ += sum(check[x])

print(sum_)