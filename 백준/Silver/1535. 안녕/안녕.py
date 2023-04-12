n = int(input()) # 사람수
# idx 조정을 위하여, 0을 추가
L = [0] + list(map(int, input().split())) # 닳을 체력
J = [0] + list(map(int, input().split())) # 오를 기쁨

# 101개(0~100)의 체력바를 지닌 n + 1명의 사람(dp[0]의 사람은 허수)
dp = [[0 for _ in range(101)] for _ in range(n + 1)]
# print(dp)

# 조건
# 1. health <= 0: game-over (범위)
# 2. 인사하는 게 좋은가? 좋지 않은가? (max 함수)

# 1부터 n까지
for i in range(1, n + 1): # 사람 idx
    # 1부터 100까지
    for j in range(1, 101): # 체력
        if L[i] <= j: # 조건1
            # 조건 2
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - L[i]] + J[i])
        else:
            dp[i][j] = dp[i - 1][j]
            
# dp[n][100]은 세준이가 죽는다.
print(dp[n][99])