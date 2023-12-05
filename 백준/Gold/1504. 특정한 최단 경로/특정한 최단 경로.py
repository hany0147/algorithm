from collections import defaultdict
import heapq
import sys

input = sys.stdin.readline


def dijkstra(start, end):
    dist = [int(1e9)] * (n + 1)
    dist[start] = 0
    q = [(0, start)]

    while q:
        distance, node = heapq.heappop(q)

        if distance > dist[node]:
            continue

        for nxt_node, nxt_cost in graph[node]:
            if dist[nxt_node] > dist[node] + nxt_cost:
                dist[nxt_node] = dist[node] + nxt_cost
                heapq.heappush(q, (dist[nxt_node], nxt_node))

    return dist[end]


n, e = map(int, input().split())
graph = defaultdict(list)
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())  # flag를 심어서, 두 간선을 지나면, True입력하기

path1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
path2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n)

if path1 >= int(1e9) and path2 >= int(1e9):
    print(-1)
else:
    print(min(path1, path2))