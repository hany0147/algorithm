import sys
from collections import deque
input = sys.stdin.readline


M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(N)] for i in range(H)]
ans = 0
q = deque([])

# 0. 탐색 좌표 설정(상하좌우위아래)
dx = [0, 0, -1, 1, 0, 0]
dy = [-1, 1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def bfs():
    while q:  
        # 1. 추출
        z, x, y = q.popleft()
        # 2. 범위 설정
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0<= nx < N and 0<= ny < M and 0<= nz < H and box[nz][nx][ny] == 0:
                box[nz][nx][ny] = box[z][x][y] + 1
                q.append([nz, nx, ny])

# 익은 토마토 큐 쌓기
for z in range(H):
    for x in range(N):
        for y in range(M):
            if box[z][x][y] == 1:
                q.append([z, x, y])
bfs()

for z in range(H):
    for x in range(N):
        for y in range(M):
            # 익지 않은 토마토가 있으면
            if box[z][x][y] == 0:
                print(-1)
                exit()
            else:
                ans = max(ans, box[z][x][y])
                
print(ans - 1)