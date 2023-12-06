from collections import defaultdict
import heapq
import sys

input = sys.stdin.readline


def dijkstra(start):
    infection = [INF] * (n + 1)
    infection[start] = 0
    q = [(0, start)]
    while q:
        time, node = heapq.heappop(q)

        if infection[node] < time:
            continue
        for nxt_node, need_time in graph[node]:
            if infection[nxt_node] > infection[node] + need_time:
                infection[nxt_node] = infection[node] + need_time
                heapq.heappush(q, (infection[nxt_node], nxt_node))

    max_time = 0
    cnt = 0
    for i in infection:
        if i != INF:
            cnt += 1
            max_time = max(max_time, i)

    return [cnt, max_time]


t = int(input())
for _ in range(t):
    n, d, c = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))
    INF = int(1e9)

    print(*dijkstra(c))