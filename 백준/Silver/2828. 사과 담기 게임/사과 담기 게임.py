n, m = map(int, input().split()) # n 칸, 왼쪽부터 m칸을 차지하는 바구니
j = int(input()) # 사과의 개수
cnt = 0 # 카운팅 초기값
cur = 1 # 시작은 무조건 1

for i in range(j):                     
    apple = int(input())
    # 범위 고려   
    # 바구니가 사과 위치를 포함하면? 
    # 움직이지 않아도 되므로 조건을 굳이 입력할 필요가 없다.                                
    if cur <= apple < cur + m: 
        continue

    # 바구니가 사과 왼쪽에 위치한다면? 해당 위치가 포함되는 칸만큼 전진
    elif cur < apple:
        cnt += apple - (cur + m - 1)
        cur = apple - m + 1

    # 바구니가 사과 오른쪽에 위치한다면? 후진
    elif cur > apple:   
        cnt += cur - apple
        cur = apple
print(cnt)