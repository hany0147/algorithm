from collections import deque

def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n + 1)]
    # 그래프를 만든다.
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    # 전력망을 끊는다.
    for a, b in wires:
        visited = [False] * (n + 1)
        graph[a].remove(b)
        graph[b].remove(a)
        # bfs 탐색으로 각 그룹의 개수를 센다.
        #. 서로 뺀다음에 제일 작은 수를 answer로 만든다.
    
        tmp = abs(bfs(a, graph, visited) - bfs(b, graph, visited))
        answer = min(tmp, answer)
        
        graph[a].append(b)
        graph[b].append(a)

    return answer

def bfs(start, graph, visited):
    q = deque([start])
    cnt = 0
    
    visited[start] = True
    
    while q:
        node = q.popleft()
        cnt += 1
        for adj in graph[node]:
            if not visited[adj]:
                visited[adj] = True
                q.append(adj)
    
    return cnt