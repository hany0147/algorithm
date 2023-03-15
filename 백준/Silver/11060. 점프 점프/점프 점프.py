import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
jumps = list(map(int, input().split()))

# 끝끝내 n번째에 가지 못하면 -1 출력
# 완전탐색(모든 경우의 수)으로 n번째로 가는 최소값을 구하라.
# dfs냐, bfs냐?
# 그래프를 그려봤을 떄, 같은 층을 탐색하며 가는 게 더 적합하므로 bfs

# 1. 방문 지점을 체크하는 방법 + 몇 번의 점프로 해당 지점까지 갈 수있는지 기록

## 현재 위치 인덱스와 가용 점프 횟수
cur, jump = 0, 0

## 자료구조 '큐'를 활용하기 위한 셋팅
queue = deque()
queue.append((cur, jump))
# print(queue)

## 방문 기록지 셋팅
visited = []

## bfs 시전

while queue: # 큐가 빌 때까지
    cur, jump = queue.popleft() # 현 위치와 가용 점프 횟수
	
    # jumps[cur]가 마지막이라면 jump를 프린트하고 while을 끝내라.
    # 근데 만약 exit()가 발휘되지 않는다면 while문 바깥에 print(-1)
    if cur == N - 1:
       print(jump)
       sys.exit()

    # 해당 위치의 점프 경우의 수를 모두 돌린다.
    for i in range(1, jumps[cur] + 1):

        # 다음 위치로 셋팅해주고
        new_cur = cur + i
        # print(new_cur)

        # 그 위치가 visited에 포함되어 있지 않다면
        if new_cur not in visited:
            # 해당 위치의 점프 경우의 수를 합한 값과, 점프 횟수 + 1
            queue.append((new_cur, jump + 1))
            # print(queue)
            visited.append(new_cur)
            # print(visited)


# 2. 끝끝내 방문하지 못하면 -1
print(-1)