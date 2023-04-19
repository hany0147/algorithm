import sys
input = sys.stdin.readline

n, k = map(int, input().split())
bag = [(0, 0)]
for _ in range(n):
    w, v = map(int, input().split())
    bag.append((w, v))
# 무게: bag[i][0], 가치: bag[i][1]
dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        weight = bag[i][0]
        value = bag[i][1]

        # 들 수 있는 경우보다 물건의 무게가 무거울 경우
        if j < weight:
            # 이전 가방의 최적값 그대로 대입
            dp[i][j] = dp[i - 1][j]
        # 아니라면
        else:
            # 이전 가방의 최적 값 vs 현 물건 가치 + 이전 물건에서 무게 - 물건 무게를 했을 때의 최적 값
            dp[i][j] = max(value + dp[i - 1][j - weight], dp[i - 1][j])
print(dp[n][k])