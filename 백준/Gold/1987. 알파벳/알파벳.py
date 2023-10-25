import sys
input = sys.stdin.readline

r, c = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]
visited = set()

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
ans = 0

def dfs(x, y, cnt):
    global ans

    ans = max(ans, cnt)
    visited.add(graph[x][y])

    for i in range(4):
        nr = x + dr[i]
        nc = y + dc[i]
        if 0 <= nr < r and 0 <= nc < c:
            if graph[nr][nc] not in visited:
                dfs(nr, nc, cnt + 1)
    visited.remove(graph[x][y])    

dfs(0, 0, 1)
print(ans)