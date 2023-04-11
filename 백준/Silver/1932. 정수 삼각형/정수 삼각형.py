n = int(input())
dp = []
for _ in range(n):
    dp.append(list(map(int, input().split())))
# print(dp)
# dp[0] = dp[0][0]
# dp[1] = dp[0][0] + dp[1][0] or dp[0][0] + dp[1][1]
# dp[2] = max(dp[1][0] + dp[2][1], dp[1][1] + dp[2][1])
# 양 끝은 쭉 내려가면 되고, 가운데들은 max로 선별해야함

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] += dp[i - 1][j]
        elif j == i:
            dp[i][j] += dp[i - 1][j - 1]
        else:
            dp[i][j] += max(dp[i - 1][j], dp[i - 1][j - 1])
print(max(dp[n - 1]))