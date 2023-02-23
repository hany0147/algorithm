import sys
input = sys.stdin.readline
sys.setrecursionlimit(2500)

# 수업시간에 배운대로 하면 풀 수 없다. 왜냐하면 dfs 한 번 돌 때마다 카운팅 해야 하는
# 문제이기 때문

# 함수 만들기(재귀형식으로)
def dfs(start):
    visited[start] = True
    for i in lst[start]: # 인접 정점 확인
        if not visited[i]: # 방문하지 않은 경우, 
            dfs(i) # 해당 dfs를 돌린다.

N, M = map(int, input().split()) # 정점 개수 n, 간선 개수 m
lst = [[] for _ in range(N + 1)] # 정점 0을 만들기 위해 1을 추가
visited = [False] * (N + 1)
cnt = 0

for _ in range(M):
    v1, v2 = map(int, input().split())
    lst[v1].append(v2)
    lst[v2].append(v1)
# print(lst)

for n in range(1, N + 1):
    if not visited[n]:
        dfs(n)
        # print(n)
        # print(visited)
        cnt += 1
print(cnt)