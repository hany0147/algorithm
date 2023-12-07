import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline
n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
INF = int(1e9)


def dijkstra(start):
    eat = [INF] * (n + 1)
    eat[start] = 0
    q = [(0, start)]

    while q:
        eating, node = heapq.heappop(q)

        if eat[node] < eating:
            continue

        for nxt, cow in graph[node]:
            if eat[nxt] > eat[node] + cow:
                eat[nxt] = eat[node] + cow
                heapq.heappush(q, (eat[nxt], nxt))
    return eat[n]


print(dijkstra(1))