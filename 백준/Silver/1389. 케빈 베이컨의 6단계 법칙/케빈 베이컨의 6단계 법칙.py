import sys
input = sys.stdin.readline
n, m = map(int, input().split())
INF = 1e9
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
# print(graph)

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
# print(graph)

# 각 index별로 총합을 구해서 최솟값을 구하되, 값이 동일하면 작은 index를 출력한다.
min = 1e9
min_index = n
for a in range(n, 0, -1):
    sum_friend = 0
    for b in range(n, 0, -1):
        sum_friend += graph[a][b]
    if min >= sum_friend:
        min = sum_friend
        min_index = a

print(min_index)