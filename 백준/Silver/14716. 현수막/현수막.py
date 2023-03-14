import sys
from pprint import pprint
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x, y):
    if x < 0 or x >= M or y < 0 or y >= N:
        return False
    

    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x + 1, y + 1)
        dfs(x + 1, y - 1)
        dfs(x, y + 1)
        dfs(x, y - 1)
        dfs(x - 1, y + 1)
        dfs(x - 1, y - 1)
        return True
    return False


M, N = map(int, input().split()) # m: x, n: y

graph = []
for _ in range(M):
    nums = list(map(int, input().split()))
    graph.append(nums)
# pprint(graph)

result = 0
for x in range(M):
    for y in range(N):
        if dfs(x, y) == True:
            result += 1
print(result)