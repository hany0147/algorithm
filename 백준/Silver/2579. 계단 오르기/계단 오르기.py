n = int(input()) # 계단 개수
dp = [0] * n # 메모리제이션(301개)
stairs = [int(input()) for _ in range(n)] # 계단 리스트

if n > 2:
    # 기본적으로 0번째와 1번째는 값을 구하고 
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    # 2번째까지도 규칙이 드러나지 않는다.
    dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])
    
    # 3번째 계단부터 상기의 dp 활용 가능
    for i in range(3, n):
        # 1. i-3까지의 최댓값 + i-1 + i
        # 2. i-2까지의 최댓값 + i
        dp[i] = max(dp[i - 3] + stairs[i - 1] , dp[i - 2]) + stairs[i]
    print(dp[n - 1])
# 계단이 두 개 이하라면 둘다 무조건 밟는게 이득  
else:
    print(sum(stairs))