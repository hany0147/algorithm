import heapq
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra():
    q = []
    heapq.heappush(q, (cave[0][0], 0, 0))
    dist[0][0] = 0

    while q:
        cost, x, y = heapq.heappop(q)

        # 끝에 도달하면
        if x == n - 1 and y == n - 1:
            print(f'Problem {cnt}: {dist[x][y]}')
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                nc = cost + cave[nx][ny]

                if nc < dist[nx][ny]:
                    dist[nx][ny] = nc
                    heapq.heappush(q, (nc, nx, ny))

cnt = 1
INF = int(1e9)

while True:
    n = int(input())
    # n값이 0으로 주어지면 바로 종료
    if n == 0:
        exit()
    cave = [list(map(int, input().split())) for _ in range(n)]
    dist = [[INF] * n for _ in range(n)]

    dijkstra()
    cnt += 1
