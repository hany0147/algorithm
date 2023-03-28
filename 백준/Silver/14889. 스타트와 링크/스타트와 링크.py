import sys
input = sys.stdin.readline
N = int(input())
teams = [list(map(int, input().split())) for _ in range(N)]

# 한 팀당 N/2명이어야 한다.
# 조합문제 -> 백트래킹 알고리즘
# 조합을 하고 최소값을 구해야 한다.

# 1. 차이를 구하는 함수

visited = [False] * N
def diff():
    start = 0
    link = 0
    
    for i in range(N - 1): # 0부터 N - 2까지(N-1은 j에 해당)
        for j in range(i + 1, N): # i의 다음 수부터  N - 1까지
            # True인 경우 start 팀
            if visited[i] and visited[j]:
                start = start + teams[i][j] + teams[j][i]
            # False인 경우 link팀
            elif not visited[i] and not visited[j]:
                link = link + teams[i][j] + teams[j][i]
    return abs(start - link)

# 2. 백트래킹
min_ans = 40000 # 최소값을 max로 잡기
def dfs(level, idx, N):
    global min_ans

    # 탈출 조건: 팀내 모집 인원이 꽉 찼을 때
    if level == N // 2:
        diff_ans = diff()
        min_ans = min(diff_ans, min_ans)
        
        # 예외처리(최적화를 위함)
        if min_ans == 0: # min_ans가 0이 되는 그 순간, 아묻따 탈출
            print(min_ans)
            exit()
        return # 탈출
    
    for i in range(idx, N):
        # 한 팀만 구하면 나머지 팀을 저절로 구성됨
        if not visited[i]:
            visited[i] = True
            dfs(level + 1, i + 1, N) # 백트랙킹의 핵심, 재귀하고나서, return하게 되면 그 이후의 것부터 시작
            visited[i] = False
    return
        
dfs(0, 0, N)
print(min_ans)