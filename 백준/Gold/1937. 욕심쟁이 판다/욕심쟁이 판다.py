import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 델타 탐색, dfs, dp

# 1. dfs 정의(dp 활용)
# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    # 건넌적이 없는 경우만
    if dp[x][y] == 0:
        dp[x][y] = 1
        # 상하 좌우 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 조건
            if 0<= nx < n and 0<= ny <n:
                # 문제 조건(많은 쪽으로만)
                if matrix[x][y] < matrix[nx][ny]:
                    # 기존대로 둘것인가, 먹게 할 것인가?
                    dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
        return dp[x][y]
    # 건넜다면 그대로 산출
    else:
        return dp[x][y]

# 2. 입력 및 설정
n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
dp = [[0] * n for _ in range(n)]
cnt = 0

# 3. 결과 산출
for x in range(n):
    for y in range(n):
        cnt = max(cnt, dfs(x, y))
print(cnt)