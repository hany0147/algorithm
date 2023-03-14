import sys
sys.setrecursionlimit(10**6)
from pprint import pprint
import copy

input = sys.stdin.readline

N = int(input())
land = []

for _ in range(N):
    land.append(list(map(int, input().rstrip().split())))
# pprint(land)

## 모든 경우의 수를 구하며, 최대한 파편화 된 곳을 구하라. 즉 dfs의 개수가 많은 곳
# 수위보다 높은 곳을 찾아 연결하라.

def dfs(x, y, graph, dep):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    
    if graph[x][y] > dep and graph[x][y] < 101:
        graph[x][y] = 101
        dfs(x + 1, y, graph, dep)
        dfs(x - 1, y, graph, dep)
        dfs(x, y + 1, graph, dep)
        dfs(x, y - 1, graph, dep)
        return True
    return False

result_lst = []
for dep in range(101):
    graph = copy.deepcopy(land)
    result = 0

    for x in range(N):
        for y in range(N):
            if dfs(x, y, graph, dep) == True:
                result += 1

    result_lst.append(result)
    if result == 0:
        break
    

fin = max(result_lst)
print(fin)