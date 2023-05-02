import heapq
m, n = map(int, input().split())
miro = [list(map(int, input())) for _ in range(n)]
distance = [[1e9] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra():
    q = []
    heapq.heappush(q, (0, 0, 0))
    distance[0][0] = 0
    while q:
        cost, x, y = heapq.heappop(q)
        if cost > distance[x][y]:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < n and 0<= ny < m:
                c = cost + miro[nx][ny]
                if c < distance[nx][ny]:
                    distance[nx][ny] = c
                    heapq.heappush(q, (distance[nx][ny], nx, ny))
dijkstra()
print(distance[n - 1][m - 1])