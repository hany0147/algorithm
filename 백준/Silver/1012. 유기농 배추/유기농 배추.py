import sys
sys.setrecursionlimit(1000000000)
input = sys.stdin.readline

from pprint import pprint
def dfs(y, x):
    # 범위 설정
    if y < 0 or y >= N or x < 0 or x >= M:
        return False
    
    # 방문하지 않았다면
    if matrix[y][x] == 1:
        # 방문하고
        matrix[y][x] = 0
        # 상하좌우도 탐색
        dfs(y + 1, x)
        dfs(y - 1, x)
        dfs(y, x - 1)
        dfs(y , x + 1)
        return True
    return False


# 행렬로 해야 하는가?
# 그렇다면 상하좌우가 연결되어 있다는 게 키포인트
# 상하좌우를 스캔하고, 인접 지점에 값이 1이면서, 아직 방문하지 않은 접점이 있으면 방문
# 방문 접점에서 다시 반복


T = int(input())

for _ in range(T):
    M, N, K = map(int, input().rstrip().split()) # 가로길이, 세로길이, 배추 심어져 있는 위치의 개수
    
    visited = [False] * N
    matrix = [[0] * M for _ in range(N)]
    # pprint(matrix)
    for _ in range(K):
        x, y = map(int, input().rstrip().split())
        matrix[y][x] = 1
    # pprint(matrix)

    result = 0

    for j in range(N):
        for i in range(M):
            if dfs(j, i) == True:
                result += 1
    print(result)
