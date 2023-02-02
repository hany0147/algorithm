M = int(input()) # 컵의 위치를 바꾼 횟수 (<= 50)

ball_dict = {
    '1' : 1,
    '2' : 0,
    '3' : 0,
}

for _ in range(M):
    X, Y = input().split()
# 해당 자리에 공이 있으면, 바꾼 곳에 공을 주고, 기존은 0으로 설정한다.
    if ball_dict[X] == 1:
        ball_dict[Y] = 1
        ball_dict[X] = 0
# 만약 해당 자리에 공이 없고, 바꿀 자리에 공이 있다면, 
    elif ball_dict[Y] == 1:
        ball_dict[X] = 1
        ball_dict[Y] = 0
        
    


# 바꾼 자리에 공이 없으면, -1 출력
if 1 not in ball_dict.values():
    print(-1)
else:
    for i in range(1, 4):
        if ball_dict[str(i)] == 1:
            print(i)
