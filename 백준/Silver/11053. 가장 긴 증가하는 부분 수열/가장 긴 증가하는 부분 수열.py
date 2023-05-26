n = int(input())
lst = list(map(int, input().split()))

dp = [1] * n
for i in range(1, n):
    for j in range(i):
        # print(i, j)
        if lst[i] > lst[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))