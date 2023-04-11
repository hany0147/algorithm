n = int(input())
T = []
P = []
dp = [0] * (n + 1)
for _ in range(n):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)


# n -1부터 0까지 (idx)
# i = idx - 1
for i in range(n - 1, -1, -1):
    # 시간을 넘어서면
    if i + T[i] > n:
        # 상담 x(i가 넘어 섰으니, i + 1도 의미 없는 수)
        dp[i] = dp[i + 1]
    else:
        # max 함수(둘 중 무엇이 낫냐?)
        # 상담을 안하는 것과, 상담을 하는 것 중
        dp[i] = max(dp[i + 1], dp[T[i] + i] + P[i])
print(dp[0])