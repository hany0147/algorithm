N, X = list(map(int, input().split()))

num_list = list(map(int, input().split()))
res = []

for num in num_list:
    if num < X:
        res.append(num)

print(*res)