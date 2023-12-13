import sys
from collections import deque

input = sys.stdin.readline

N, L, R = map(int, input().split())

countries = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    countries.append(tmp)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(a, b):
    q = deque()
    temp = []
    q.append((a, b))
    temp.append((a, b))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny]:
                    if L <= abs(countries[nx][ny] - countries[x][y]) <= R:
                        visited[nx][ny] = True
                        q.append((nx, ny))
                        temp.append((nx, ny))

    return temp


day = 0

while True:
    visited = [[False] * N for _ in range(N)]
    moved = False
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                visited[r][c] = True
                moving = bfs(r, c)

                if len(moving) > 1:
                    moved = True
                    result = sum([countries[x][y] for x, y in moving]) // len(moving)
                    for a, b in moving:
                        countries[a][b] = result

    if not moved:
        print(day)
        break

    day += 1