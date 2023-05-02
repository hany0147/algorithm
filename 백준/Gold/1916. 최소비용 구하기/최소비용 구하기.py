import heapq
import sys
input = sys.stdin.readline

n = int(input()) # 도시의 개수
m = int(input()) # 버스의 개수
INF = int(1e9)
# print(type(INF)) -> class 'float'

route = [[] for _ in range(n + 1)] # 노선 정보
for _ in range(m):
    s, e, c = map(int, input().split())
    route[s].append((e, c))
distance = [INF] * (n + 1)
target_s, target_e = map(int, input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        c, now = heapq.heappop(q)
        if distance[now] < c:
            continue
        for destination, weight in route[now]:
            cost = distance[now] + weight
            if distance[destination] > cost:
                distance[destination] = cost
                heapq.heappush(q, (cost, destination))

dijkstra(target_s)
print(distance[target_e])