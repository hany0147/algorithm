import sys
sys.setrecursionlimit = 10000
input = sys.stdin.readline

# DFS
def dfs(graph1, v1, visited1):
    # 첫번째 정점(노드) 방문
    visited1[v1] = True
    print(v1, end = " ")
    # 인접 정점 체크
    for i in graph1[v1]:
        # 그런데 만약 해당 정점을 방문한 적이 없답면
        if not visited1[i]:
            # 재귀 방문
            dfs(graph1, i, visited1)

# BFS: 자료구조 '큐'를 이용하기 위해 라이브러리에서 덱을 가져온다.
from collections import deque
def bfs(graph2, v2, visted2):
    print()
    # 덱 생성
    queue = deque([v2])

    # 현재 방문한 정점 처리
    visited2[v2] = True

    # 큐가 빌때까지 반복한다.
    while queue:
        # 원소 하나 뽑기
        a = queue.popleft()
        print(a, end = ' ')
        # 인접 정점 방문
        for i in graph2[a]:
            if not visited2[i]:
                queue.append(i)
                visited2[i] = True

# 실제 풀이를 위한 입력값

n1, m1, v1 = map(int, input().rstrip().split())
n2, m2, v2 = n1, m1, v1
visited1 = [False] * (n1 + 1)
visited2 = [False] * (n2 + 1)
graph1 = [[] for _ in range(n1 + 1)]


for _ in range(m1):
    x, y = map(int, input().rstrip().split())
    graph1[x].append(y)
    graph1[y].append(x)

for N in range(1, n1 + 1):
    new = sorted(graph1[N])
    graph1[N] = new

graph2 = graph1

# print(graph1)
# print(graph2)

dfs(graph1, v1, visited1)
bfs(graph2, v2, visited2)

# 정점 번호가 작은 것을 먼저 방문!
# 간선은 양방향