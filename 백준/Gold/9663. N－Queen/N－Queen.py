import sys
input = sys.stdin.readline
n = int(input())
row = [0] * n # 퀸의 위치
cnt = 0

def check(x): # 검증
    for i in range(x):
        # 같은 위치이거나, 대각선 방향이 같다면
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            # false
            return 0
    # ture
    return 1
    
def queen(x):
    global cnt
    
    # 걸리는 거 하나 없이 마지막 줄까지 다 돌았으니, 경우의 수를 +1하고 종료
    if x == n :
        cnt += 1
        return

    # x행에 퀸 놓기    
    for i in range(n): # 0~n-1까지 탐색
        row[x] = i
        if check(x): # 검증을 통과하면 queen(x + 1) 호출
            queen(x + 1)
queen(0)
print(cnt)