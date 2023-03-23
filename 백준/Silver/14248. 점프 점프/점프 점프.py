import sys
sys.setrecursionlimit(10**6)

n = int(input()) # 돌다리의 돌 개수
check = [False] * n # 체크 리스트
jumps = list(map(int, input().split())) # 점프할 수 있는 거리
start = int(input()) - 1 # 출발점
cnt = 1 # 방문한 돌의 개수(초기값 1, 처음 밟은 위치)

# 1. dfs 함수 정의
def dfs(x):
    global cnt # 전역 변수 cnt 설정

    # 현재 정점에서 갈 수 있는 가용 범위는 +, - 오직 두 가지 위치
    for new_x in (x + jumps[x], x - jumps[x]): # new_x 새로운 정점
        if 0 <= new_x < n and check[new_x] == False: # 가능 범위 설정
            cnt += 1
            check[new_x] = True
            dfs(new_x)

dfs(start)
print(cnt)