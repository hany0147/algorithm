from collections import deque

def bfs(x, y, z):
    q = deque()
    q.append((x, y, z))

    while q:
        a, b, c = q.popleft()
        if a == n - 1 and b == m - 1:
            return visited[a][b][c]
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                # 다음 이동할 곳이 벽이고, 벽 파괴기회를 사용하지 않은 경우
                if graph[nx][ny] == 1 and c == 0:
                    visited[nx][ny][1] = visited[a][b][0] + 1
                    q.append((nx, ny, 1))
                # 다음 이동할 곳이 벽이 아니고, 한 번도 방문하지 않은 곳이라면
                elif graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                    visited[nx][ny][c] = visited[a][b][c] + 1
                    q.append((nx, ny, c))

    return -1

n, m = map(int, input().split())
graph = []
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

for i in range(n):
    graph.append(list(map(int, input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


print(bfs(0, 0, 0))